# Link Budgets 
 
A [link budget](https://en.wikipedia.org/wiki/Link_budget) is a design aid, calculated during the design of a communication system to determine the received power, to ensure that the information is received intelligibly with an adequate [signal-to-noise ratio](https://en.wikipedia.org/wiki/Signal-to-noise_ratio). The SelfieSat uses a duplex communication system to receive commands from the Mission Control Centre, and transmit data to Amateur Radio Operators, therefore we need a link budget! 

In this document, we are going to learn some of the ins and outs of a link budget and we'll try to make one. 

# Goals and Learning Objectives 📖

1️⃣ Determine what inputs are to be included in a link budget. 

2️⃣ Determine what outputs we expect from a link budget.

3️⃣ Make our own link budget. 

# Definitions and Key Terms 🔑

- [Signal-to-Noise Ratio](https://en.wikipedia.org/wiki/Signal-to-noise_ratio) (SNR): a comparison of the level of a desired signal to the level of background noise. SNR is defined as the ratio of signal power to the noise power, often expressed in decibels. A ratio higher than 1:1 (greater than 0 dB) indicates more signal than noise.
- [Energy Per Bit to Noise Power Spectral Density Ratio](https://en.wikipedia.org/wiki/Eb/N0) (Eb/No): a normalized signal-to-noise ratio (SNR) measure, also known as the "SNR per bit". 
- [Baud](https://en.wikipedia.org/wiki/Baud) (Bd): a common unit of measurement of symbol rate, which is one of the components that determine the speed of communication over a data channel. If there are precisely two symbols in the system (typically 0 and 1), then baud and bit per second (bit/s) are equivalent.
- [Equivalent Isotropically Radiated Power](https://www.everythingrf.com/community/what-is-eirp) (EIRP): a measurement of radiated output power from an ideal isotropic antenna in a single direction.
- [Isotropic Antenna](https://www.everythingrf.com/community/what-is-an-isotropic-antenna): An isotropic antenna is a theoretical antenna that radiates equally in all directions - horizontally and vertically with the same intensity. The antenna has a gain of 1 (0 dB) in the spherical space all around it and has an efficiency of 100%. An isotropic antenna is used as a reference antenna to evaluate antenna gain.

# Section 1: What Are We Trying To Do? 
At the end of the day, we are trying to determine the minimum amount of output power required at the transmitter for a given signal strength at the receiver. By creating a link budget, we will know whether we have enough power and gain in the transmission, enabling us to take action if the levels are too high or too low. If you don’t have enough power and gain, we will have a weak signal. If we have too much power and gain, we may be able to switch to a less powerful antenna or reduce your total transmission power, which can save money and energy. 

To perform an accurate calculation, we’ll need to consider all of the gains and losses involved in a particular link. The total calculation should include the following at a minimum:
- Transmitted power
- Receiver antenna gain
- Transmitter antenna gain
- Transmission feeder loss
- Receiver feeder loss
- Path and propagation loss

Based on these factors, a basic link budget equation may read as follows:

<p align='center'>
🌟 signal strength = transmitted power + gains – losses 🌟 
</p>

We can organize all these different gains and losses in a table for **both** of the **downlink** and **uplink** communication channels to completely characterize our communication link.  

# Section 2: Making the Budget
Okay, so we're going to make a couple of fancy excel spreadsheets. What are our column headings and what are the rows that we need to include? 

## 2.1 Columns
Example column headers are given below. Feel free to add more columns if you see the justification, but these are sufficient for the budget. 

| Item | Symbol | Unit | Value | Source | Notes |
| --- | --- | --- | --- | --- | --- |
| Frequency | f | MHz | 443 | Input | UHF band, access to amateur radio operators | 

- Item:
- Symbol:
- Units:
- Value:
- Source:
- Notes:

## 2.2 Rows 
Now with our header in place, lets move on to the rows. Example row sections are given below alongside our headers. Feel free to add more rows if there are further details to be included, or to simplify calculations. 

| Item | Symbol | Unit | Value | Source | Notes |
| --- | --- | --- | --- | --- | --- |
| SYSTEM | | | | | |
| Frequency | f | MHz | 443 | Input | UHF band, access to amateur radio operators | 
| ... | ... | ... | ... | ... | ... |
| TRANSMISSION | | | | | |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| LOSSES | | | | | |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| RECEPTION | | | | | |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| NOISE | | | | | |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| MARGINS | | | | | |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

### 2.2.1 SYSTEM
- Frequency
- Wavelength

### 2.2.2 TRANSMISSION
- Transmitter Power
- Transmitter Antenna Gain
- Transmitter Line Loss
- Transmit Antenna Pointing Loss
- Equiv. Isotropic Radiated Power

### 2.2.3 LOSSES
- Total Propagation Path Length
- Space Loss
- O2 absorption at Frequency
- H2O absorption at Frequency
- Atmospheric Absorption loss
- Polarization Loss
- Propagation & Polarization Loss

### 2.2.4 RECEPTION
- Peak Receive Antenna Gain
- Receive Antenna Pointing Loss
- Receive Antenna Gain

### 2.2.5 NOISE
- Antenna Noise Temperature
- Line Loss Noise
- Receiver Noise
- System Noise
- System Noise Temperature

### 2.2.6 MARGINS
- Data Rate
- Eb/No
- Carrier-to-Noise Density Ratio
- Bit Error Rate
- Required Eb / No
- Implementation Loss
- Margin
- Power Received
- Receiver Sensitivity
- Margin of Power Received 


# Section 3: SMAD Detailed Steps 
The satellite bible [Space Mission Analysis and Design (SMAD)](https://queensuca.sharepoint.com/:b:/t/GROUP-QSET/EetrWtbsPE9Mr-KgKMFOANgBPXy5Lkg9ayXt6OVcL1NoDA?e=N3Y3Kt) has really good information regarding link budget design. Bit of a read, but worth it. Their detailed procedure for a downlink design is as follows:

1. Select carier frequency, based on spectrum availability, FCC allocations, and mission requirements.
2. Select the satellite transmitter power, based on satellite size and power limits.
3. Estimate RF losses between transmitter and satellite antennas. (Usually between - 1 and -3 dB.)
4. Determine the required beamwidth for the satellite antenna, depending on the satellite orbit, satellite stabilization, and ground coverage area. 
5. Estimate the maximum antenna pointing offset angle, based on coverage angle, satellite stabilization error, and stationkeeping accuracy.
6. Calculate transmit antenna gain toward the ground station, using Eqs. (13-20) and (13-21). You might also want to check the antenna diameter, using Eq. (13-19), to see if it will fit on the satellite.
7. Calculate space loss, using Eq. (13-23a). This is determined by satellite orbit and ground-station location.
8. Estimate propagation absorption loss due to the atmosphere using Fig. 13-10, dividing the zenith attenuation by the sine of the minimum elevation angle (e.g. 10 deg) from the ground station to the satellite. (Consider rain attenua- tion later.) I would also add a loss of 0.3 dB to account for polarization mismatch for large ground antennas. Using a radome adds another 1 dB loss.
9. Select the ground station antenna diameter and estimate pointing error. If autotracking is used, let the pointing error be 10% of the beamwidth. Use Eq. (13-21) to calculate the antenna beamwidth.
10. Calculate the receive antenna gain toward the satellite. For FireSat we used antenna efficiency, 77,of 0.55.
11. Estimate the system noise temperature (in clear weather), using Table 13-10.
12. Calculate Eb/No for the required data rate, using Eq. (13-14).
13. Using Fig. 13-9, look up E b / No required to achieve desired BER for the selected modulation and coding technique. The downlink for FireSat is modu- lated with BPSK and the uplink is BPSK/PM. See Table 13-11.
14. Add 1 to 2 dB to the theoretical value given in Fig. 13-9 for implementation losses.
15. Calculate the link margin the difference between the expected value of Eb/No calculated and the required Eb/No (including implementation loss).
16. Estimate the degradation due to rain, using Fig. 13-11 and Eq. (13-27).
17. Adjust input parameters until the margin is at least 3 dB greater than the esti- mated value for rain degradation, depending on confidence in the parameter estimates.

# Relevant Documentation and Resources

- [CAN-SBX Link Budget](https://queensuca.sharepoint.com/:x:/t/GROUP-QSET/EXgS7Tc93c9LmauqfWks098BMDNnGnvrHXVt8gIhve7oLg?e=LhSWYF)
- [SMAD - Communication Architecture](https://queensuca.sharepoint.com/:b:/t/GROUP-QSET/EetrWtbsPE9Mr-KgKMFOANgBPXy5Lkg9ayXt6OVcL1NoDA?e=N3Y3Kt)
