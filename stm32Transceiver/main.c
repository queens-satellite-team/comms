/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */

// #pragma warning(disable:) // use this to "fix" the warnings if they get annoying. Enter the warning code after disable:
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "string.h"

#include "NRF24L01.h"
/* COMMANDS FROM NRF DRIVER:
 * void CS_Select (void)
 * 		-- Pulls CS down
 * void CS_UnSelect (void)
 * 		-- Pulls CS up
 * void CE_Enable (void)
 * 		-- Pulls CE up
 * void CE_Disable (void)
 * 		-- Pulls CE down
 * void nrf24_WriteReg (uint8_t Reg, uint8_t Data)
 * 		-- Sets DATA at address REG
 * void nrf24_WriteRegMulti (uint8_t Reg, uint8_t *data, int size)
 * 		-- Sets a whole bunch of sequential registers equal to an oversized DATA array
 * uint8_t nrf24_ReadReg (uint8_t Reg)
 * 		-- Returns the state of register REG
 * void nrf24_ReadReg_Multi (uint8_t Reg, uint8_t *data, int size)
 * 		-- Returns an array of register states
 * void nrfsendCmd (uint8_t cmd)
 * 		-- Send a operational command
 * void nrf24_reset(uint8_t REG)
 * 		-- Resets flags if REG = 0x07, otherwise resets the registry entirely
 * void NRF24_Init (void)
 * 		-- initializes the board, ready to receive
 * void NRF24_TxMode (uint8_t *Address, uint8_t channel)
 * 		-- Sets the transceiver to transmit to ADDRESS on rf channel CHANNEL
 * uint8_t NRF24_Transmit (uint8_t *data)
 * 		-- Transmits data
 * void NRF24_RxMode (uint8_t *Address, uint8_t channel)
 * 		-- Sets the transceiver to receive to ADDRESS on rf channel CHANNEL
 * uint8_t isDataAvailable (int pipenum)
 * 		-- Checks for non-zero on data pipe. Returns 1 if true.
 * void NRF24_Receive (uint8_t *data)
 * 		-- Grabs data from the queue and stores it in DATA
 * void NRF24_ReadAll (uint8_t *data)
 * 		-- Read all registers, store in DATA
 */
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
SPI_HandleTypeDef hspi3;

UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART2_UART_Init(void);
static void MX_SPI3_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

uint8_t RxAddress[] = {0x00,0xDD,0xCC,0xBB,0xAA};
uint8_t RxData[32];


uint8_t data[50];

//uint8_t TxAddress[] = {0xEE,0xDD,0xCC,0xBB,0xAA};
//uint8_t TxData[] = "Hello World\n";

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */
  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART2_UART_Init();
  MX_SPI3_Init();
  /* USER CODE BEGIN 2 */

  NRF24_Init();
  /*
  int8_t rfAddress = 6;
  int8_t rfChannel = 0x06;
  NRF24_RxMode(&rfAddress, rfChannel);
  */

/*
  // test print:
  uint8_t testprint[4] = {0x04, 0x08, 0xa2, 0xff};
  HAL_UART_Transmit(&huart2, (int)testprint, strlen((char *)testprint), 1000);
  // get all registry data
  NRF24_ReadAll(data);
  // print all data:
  HAL_UART_Transmit(&huart2, (char)data, strlen((char *)data), 1000);*/
  uint8_t ttdata[50]; // test - storage of entire slave registry
  for (int i = 0; i<50; i++) // fill testtestdata with 0s
	  ttdata[i] = 255;
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */

	  NRF24_ReadAll(&ttdata);
	  // print all data:
	 // HAL_UART_Transmit(&huart2, (char)ttdata, strlen((char *)ttdata), 1000);
	  if (isDataAvailable(2) == 1)
	  {
		  NRF24_Receive(RxData);
		 // HAL_UART_Transmit(&huart2, RxData, strlen((char *)RxData), 1000);
	  }/*
	  if(HAL_GPIO_ReadPin(GPIOB, GPIO_PIN_13)) // read button
	  {
		  // turn on LED
		  HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5); // turn LD2 on
		  // transmit hello world on channel 10:
		  char hworldChar[] = {'H','E','L','L','O',' ','W','O','R','L','D'};
		  uint8_t hworldUint[11];
		  for(int i = 0; i < 1; i++)
		  		  hworldUint[i] = (uint8_t)hworldChar[i];
		  hworldUint[11] = 0;
		  NRF24_TxMode(&rfAddress, rfChannel);
		  NRF24_Transmit(&hworldUint);
		  // leave LED on for more second
		  HAL_Delay(1000);
		  HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5); // turn LD2 off
		  HAL_Delay(1000);
	 // }*/


/*
	  // broadcast hello world
	  NRF24_TxMode (&rfAddress, rfChannel);

	  uint8_t hworldUint[12];
	  NRF24_ReadAll(&ttdata); // this warning can be ignored. Enough said.

	  NRF24_ReadAll(&ttdata);
	  HAL_Delay(1000);*/
//	  if (NRF24_Transmit(TxData) == 1)
//	  {
//		  HAL_GPIO_TogglePin(GPIOF, GPIO_PIN_9);
//	  }
//
//	  HAL_Delay(1000);
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);
  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 16;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 4;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief SPI3 Initialization Function
  * @param None
  * @retval None
  */
static void MX_SPI3_Init(void)
{

  /* USER CODE BEGIN SPI3_Init 0 */

  /* USER CODE END SPI3_Init 0 */

  /* USER CODE BEGIN SPI3_Init 1 */

  /* USER CODE END SPI3_Init 1 */
  /* SPI3 parameter configuration*/
  hspi3.Instance = SPI3;
  hspi3.Init.Mode = SPI_MODE_MASTER;
  hspi3.Init.Direction = SPI_DIRECTION_2LINES;
  hspi3.Init.DataSize = SPI_DATASIZE_8BIT;
  hspi3.Init.CLKPolarity = SPI_POLARITY_LOW;
  hspi3.Init.CLKPhase = SPI_PHASE_1EDGE;
  hspi3.Init.NSS = SPI_NSS_SOFT;
  hspi3.Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_8;
  hspi3.Init.FirstBit = SPI_FIRSTBIT_MSB;
  hspi3.Init.TIMode = SPI_TIMODE_DISABLE;
  hspi3.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
  hspi3.Init.CRCPolynomial = 10;
  if (HAL_SPI_Init(&hspi3) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN SPI3_Init 2 */

  /* USER CODE END SPI3_Init 2 */

}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 115200;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOA, SPI3_SSEL_Pin|LD2_Pin|SPI3_CE_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : B1_Pin */
  GPIO_InitStruct.Pin = B1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(B1_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : SPI3_SSEL_Pin LD2_Pin SPI3_CE_Pin */
  GPIO_InitStruct.Pin = SPI3_SSEL_Pin|LD2_Pin|SPI3_CE_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

