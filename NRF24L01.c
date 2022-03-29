/*
 * NRF24L01.c
 *
 *  Created on: Feb 12, 2022
 *      Author: jacoblambert
 */


#include "stm32f4xx_hal.h"
#include "NRF24L01.h"

extern SPI_HandleTypeDef hspi1;
#define NRF24_SPI &hspi1

//define the CE and CSN Pin -----> need to define the Pin
#define NRF_CE_PORT GPIOD
#define NRF_CE_PIN GPIO_PIN_5

#define NRF_CSN_PORT GPIOD
#define NRF_CSN_PIN GPIO_PIN_4

//to select and unselect the  device (like open/close device)
void CS_Select(void){
	HAL_GPIO_WritePin(NRF_CSN_PORT, NRF_CSN_PIN, GPIO_PIN_RESET);
}
void CS_unSelect(void){
	HAL_GPIO_WritePin(NRF_CSN_PORT, NRF_CSN_PIN, GPIO_PIN_SET);
}


//to chip enable
void CE_Disable(void){
	HAL_GPIO_WritePin(NRF_CE_PORT, NRF_CE_PIN, GPIO_PIN_RESET);
}
void CE_Enable(void){
	HAL_GPIO_WritePin(NRF_CE_PORT, NRF_CE_PIN, GPIO_PIN_SET);
}


//to write a single byte to register
void nrf24_writeReg (uint8_t Reg, uint8_t Data){
	uint8_t buf[2];

	//in datasheet 5th bit in register must be a 1 (pg 46)
	buf[0] = Reg|1<<5;

	buf[1] = Data;

	//call the CS pinlow to select the device
	CS_Select();

	//transmit to SPI
	HAL_SPI_Transmit(NRF24_SPI, buf, 2, 1000);

	//pull cs high to release
	CS_unSelect();

}

//write multiple bytes starting from a particular register
void nrf24_writeRegMulti(uint8_t Reg, uint8_t *data, int size){
	uint8_t buf[2];

	//in datasheet 5th bit in register must be a 1 (pg 46)
	buf[0] = Reg|1<<5;

	//call the CS pinlow to select the device
	CS_Select();

	//transmit to SPI
	HAL_SPI_Transmit(NRF24_SPI, buf, 2, 100);
	HAL_SPI_Transmit(NRF24_SPI, data, size, 1000);

	//pull cs high to release
	CS_unSelect();
}

//read data from a particular register
uint8_t nrf24_readReg(uint8_t Reg){

	uint8_t data=0;

	//call the CS pinlow to select the device
	CS_Select();

	//transmit to SPI, but only Reg since we done need any more bits
	HAL_SPI_Transmit(NRF24_SPI, &Reg, 1, 100);
	HAL_SPI_Receive(NRF24_SPI, &data, 1, 100);

	//pull cs high to release
	CS_unSelect();

	return data;
}

//read multiple bytes from register
void nrf24_readRegMulti (uint8_t Reg, uint8_t *data, int size){
	//transmit to SPI, but only Reg since we done need any more bits
	HAL_SPI_Transmit(NRF24_SPI, &Reg, 1, 100);
	HAL_SPI_Recieve(NRF24_SPI, data, 1, 1000);

	//pull cs high to release
	CS_unSelect();
}

//send command to NRF
void nrf_sendCmd(uint8_t cmd){
	//call the CS pinlow to select the device
	CS_Select();

	//transmit to SPI
	HAL_SPI_Transmit(NRF24_SPI, &cmd, 2, 1000);

	//pull cs high to release
	CS_unSelect();
}

//intialize the nrf24
void NRF24_Init(void){
	//disable the chip before config
	CE_Disable();
	CS_unSelect();

	//configuring registers (section 9.1)
	nrf24_writeReg(CONFIG, 0); // configure the  register
	nrf24_writeReg(EN_AA, 0); //not using auto acknowledgement

	//disable all the pipes
	nrf24_writeReg(EN_RXADDR, 0);

	//set the address width (5 bits)
	nrf24_writeReg(SETUP_AW, 0x03);

	//disable automatic read transmission
	nrf24_writeReg(SETUP_RETR, 0);

	//transmission channel selection set to 0, will be configured for TX RX later
	nrf24_writeReg(RF_CH, 0);

	//set data rate - max (2 Mbps and power of 0dB)
	nrf24_writeReg(RF_SETUP, 0x0E);

	//enable the chip after the configuration
	CE_Enable();

}


//SET UP THE TX MODE

void NRF24_TXMode(uint8_t *Address, uint8_t channel){
	//diable the chip before config
	CE_Disable();

	//set up the rf channel
	nrf24_writeReg(RF_CH, channel);

	//set up the tx address
	nrf24_writeRegMulti(TX_ADDR, Address, 5);

	//power up the device
	uint8_t config = nrf24_readReg(CONFIG);
	config = config | (1<<1);
	nrf24_writeReg(CONFIG, config);

	//now enable device
	CE_Enable();
}

//transmit data
uint8_t NRF24_Transmit(uint8_t *data){
	uint8_t cmdtosend = 0;
	//select the device
	CS_Select();

	//payload command
	cmdtosend = W_TX_PAYLOAD;
	HAL_SPI_Transmit(NRF24_SPI, &cmdtosend, 1, 100);
	//send payload
	HAL_SPI_Transmit(NRF24_SPI, data, 32, 100);

	//unselect
	CS_unSelect();

	//check if transmission was successful using  TX FIFO reg 4
	HAL_Delay(1);

	uint8_t fifostatus = nrf24_readReg(FIFO_STATUS);

	//need the second part since there is no way to tell if it didnt work
	//or was unplugged, check that 00 since it will be 11 if unplugged
	if((fifostatus&(1<<4)) && (!(fifostatus&(1<<3)))){
		cmdtosend = FLUSH_TX;
		nrf_sendCmd(cmdtosend);
		return 1;
	}

	return 0; //means failed


}

void NRF24_RXMode(uint8_t *Address, uint8_t channel){
	//diable the chip before config
		CE_Disable();

		//set up the rf channel
		nrf24_writeReg(RF_CH, channel);

		//to choose datapipe1 and make sure to not overwrite
		uint8_t en_rxaddr = nrf24_readReg(EN_RXADDR);
		en_rxaddr = en_rxaddr| (1<<1);
		nrf24_writeReg(EN_RXADDR, en_rxaddr);


		nrf24_writeRegMulti(RX_ADDR_P1, Address, 5);

		nrf24_writeReg(RX_PW_P1, 32); //32 byte payload

		//power up the device in rx mode
		uint8_t config = nrf24_readReg(CONFIG);
		config = config | (1<<1) | (1<<0);
		nrf24_writeReg(CONFIG, config);

		//now enable device
		CE_Enable();
}

uint8_t isDataAvailable(int pipenum){
	uint8_t status = nrf24_readReg(STATUS); //get status
	if((status&(1<<6)) && (status&(pipenum<<1))){
		//clear rx dr bit
		nrf24_writeReg(STATUS, (1<<6));
		return 1;
	}
	return 0;
}

void NRF24_Receive(uint8_t *data){
	uint8_t cmdtosend = 0;
	//select the device
	CS_Select();

	//payload command
	cmdtosend = R_RX_PAYLOAD;
	HAL_SPI_Transmit(NRF24_SPI, &cmdtosend, 1, 100);
	//send payload
	HAL_SPI_Receive(NRF24_SPI, data, 32, 100);

	//unselect
	CS_unSelect();

	//check if transmission was successful using  TX FIFO reg 4
	HAL_Delay(1);

	cmdtosend = FLUSH_RX;
	nrf_sendCmd(cmdtosend);

}

