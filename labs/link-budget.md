# Link Budgets 
 
A [link budget](https://en.wikipedia.org/wiki/Link_budget) is a design tool, developed during the design of a communication system to determine **1)** the received power from an incoming signal, and **2)** to ensure that the signal is received intelligibly with an adequate [signal-to-noise ratio](https://en.wikipedia.org/wiki/Signal-to-noise_ratio). In the design of QSET's SelfieSat, there is a requirement for a duplex communication system to send and receive data and commands from the Mission Control Centre and Amateur Radio Operators, therefore we need to make a link budget!

# Goals and Learning Objectives 📖

1️⃣ Determine what inputs are to be included in a link budget. 

2️⃣ Determine what outputs we expect from a link budget.

3️⃣ Make our own link budget. 

# Definitions and Key Terms 🔑

- [Transmitter](https://en.wikipedia.org/wiki/Transmitter): an electronic device which produces radio waves with an antenna. The transmitter itself generates a radio frequency alternating current, which is applied to the antenna. When excited by this alternating current, the antenna radiates radio waves.
- [Signal-to-Noise Ratio](https://en.wikipedia.org/wiki/Signal-to-noise_ratio) (SNR): a comparison of the level of a desired signal to the level of background noise. SNR is defined as the ratio of signal power to the noise power, often expressed in decibels. A ratio higher than 1:1 (greater than 0 dB) indicates more signal than noise.
- [Energy Per Bit to Noise Power Spectral Density Ratio](https://en.wikipedia.org/wiki/Eb/N0) (Eb/No): a normalized signal-to-noise ratio (SNR) measure, also known as the "SNR per bit". 
- [Baud](https://en.wikipedia.org/wiki/Baud) (Bd): a common unit of measurement of symbol rate, which is one of the components that determine the speed of communication over a data channel. If there are precisely two symbols in the system (typically 0 and 1), then baud and bit per second (bit/s) are equivalent.
- [Equivalent Isotropically Radiated Power](https://www.everythingrf.com/community/what-is-eirp) (EIRP): a measurement of radiated output power from an ideal isotropic antenna in a single direction.
- [Isotropic Antenna](https://www.everythingrf.com/community/what-is-an-isotropic-antenna): An isotropic antenna is a theoretical antenna that radiates equally in all directions - horizontally and vertically with the same intensity. The antenna has a gain of 1 (0 dB) in the spherical space all around it and has an efficiency of 100%. An isotropic antenna is used as a reference antenna to evaluate antenna gain.
- [Free Space Path Loss](https://en.wikipedia.org/wiki/Free-space_path_loss): the loss between two isotropic antennas in free space. It does not include any power loss in the antennas themselves due to imperfections such as resistance. 
- [Contemporary Transmission Equation](https://en.wikipedia.org/wiki/Friis_transmission_equation#cite_note-Friis-2): characterizes antenna performance over the contemporary use of directivity and gain metrics, can be used instead of Friis Trnasmission Equation if some parameters are not known. 
- [Friis Transmission Equation](https://en.wikipedia.org/wiki/Friis_transmission_equation): equating the power at the terminals of a receive antenna as the product of power density of the incident wave and the effective aperture of the receiving antenna under idealized conditions given another antenna some distance away transmitting a known amount of power.
- [Effective Antenna Aperture](https://www.everythingrf.com/rf-calculators/effective-antenna-aperture-calculator): The effective antenna aperture/area is a theoritical value which is a measure of how effective an antenna is at receiving power. The effective aperture/area can be calculated by knowing the gain of the receiving antenna.
- [Modulation](https://en.wikipedia.org/wiki/Modulation): the process of varying one or more properties of a periodic waveform, called the carrier signal, with a separate signal called the modulation signal that typically contains information to be transmitted.
- [Carrier Signal/Wave](https://en.wikipedia.org/wiki/Carrier_wave): a waveform that is modulated (modified) with an information-bearing signal for the purpose of conveying information. This carrier wave usually has a much higher frequency than the input signal does. The purpose of the carrier is to transmit the information through space.

# Section 1: What Are We Trying To Do? 
At the end of the day, we are trying to determine the minimum amount of output power required at the transmitter for a given signal strength at the receiver. By creating a link budget, we will know whether we have enough power and gain in the transmission, enabling us to take action if the levels are too high or too low. If you don’t have enough power and gain, we will have a weak signal and it will not be able to be discerned from the ambient noise around us. If we have too much power and gain, we may be able to switch to a smaller / less powerful antenna or reduce your total transmission power, which can save money and energy. 

To perform an accurate calculation, we’ll need to consider all of the gains and losses involved in a particular link. The total calculation should include the following at a minimum:
- Transmitted power
- Transmitter antenna gain
- Receiver Sensitivity 
- Receiver antenna gain
- Transmission feeder loss
- Receiver feeder loss
- Path and propagation loss

Based on these factors, a basic link budget equation may read as follows:

<p align='center'>
🌟 signal received = (transmitted power + gains – losses) / (background-noise) 🌟 
</p>

We can organize all these different gains and losses in a table for **both** of the **downlink** and **uplink** communication channels to completely characterize our communication link.  

# Section 2: Making the Budget
Okay, so we're going to make a couple of fancy excel spreadsheets. The thought process behind developing these is going to be:
1. What are the column headings?
2. What are the sections that we need to include for the rows?
3. What rows needs to be filled within those different sections?
4. How do we get the information to fill in those rows? 

## 2.1 Column Headings
We need to describe each item in the link budget so our header will outline what we need to know about each item. An example column header is given, as well as explanation for each of the headers below. Feel free to add more columns if you see the justification, but these are sufficient for really any budget. 

| Name | Symbol | Unit | Value | Source | Notes |
| --- | --- | --- | --- | --- | --- |
| Frequency | f | MHz | 443 | Input | UHF band, access to amateur radio operators |

- **Name**: Things have names, include them so everyone knows what you are refering to. 
- **Symbol**: The link budget is basically a set of calculations layed out in a table, so including symbols will make refering to different items within the **Source** and/or **Notes** sections easier.  
- **Units**: easy to get calculations wrong when we are not consistent with units. Try to keep everything in **dBm**, **dBi**, and SI units to make calculations more clear. 
- **Value**: finally the numerical value of the item, what we really care about.  
- **Source**: can be either user input, estimate, calculated, or from a datasheet. Since this is part of the design process, there is going to be changes back and forth, and more than one person working on it, thus we need to know where each item comes from. 
- **Notes**: can include any kind of link, justification, or further explanation. This is good to include as you are not always there to explain yourself.

## 2.2 Row Sections 
Now with our header in place, lets move on to the rows. We can take a moment to think back on what is happening with a communication link to guide us on what sections we need to include. There is a source that is sending a signal, it travels some distance, and then is received by a sink. So we have to include a `TRANSMISSION` section, a `LOSS` section, as well as a `RECEPTION` section. Cool, now lets think again on what we are trying to get out of a link budget: **1)** the received power from an incoming signal, and **2)** to ensure that the signal is received intelligibly with an adequate [signal-to-noise ratio](https://en.wikipedia.org/wiki/Signal-to-noise_ratio). So we will include a `NOISE` section, as well as a `MARGINS` section where we will show the final output values. I think its also useful to have a section for `SYSTEM PARAMETERS` that includes general information such as the frequency and wavelength of the communication link. 

An example table with sections is given below alongside our header from before. 

| Item | Symbol | Unit | Value | Source | Notes |
| --- | --- | --- | --- | --- | --- |
| SYSTEM PARAMETERS | | | | | |
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

## 2.3 Row Details
Okay, so we have a header and an outline of some of the sections to include. But what needs to be included in these sections? Below is a list of the required parameters to include in each section. It is not exhaustive as you can add more detail if desired, but including all of these is sufficient to identify a margin for the communication link. 

### 2.2.1 SYSTEM PARAMETERS
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

## 2.4 SMAD Steps For Making a Link Budget 
Okay, so how do we go about finding the values and equations to be used in all these items now? Well we have to do some research and a good place to start is the satellite bible [Space Mission Analysis and Design (SMAD)](https://queensuca.sharepoint.com/:b:/t/GROUP-QSET/EetrWtbsPE9Mr-KgKMFOANgBPXy5Lkg9ayXt6OVcL1NoDA?e=N3Y3Kt). It has really good information regarding link budget design; bit of a read, but worth it. Their detailed procedure for a downlink design is as follows:

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
- [The Jan King Link Budget Spread Sheets](http://www.amsatuk.me.uk/iaru/spreadsheet.htm)
