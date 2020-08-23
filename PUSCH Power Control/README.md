# PUSCH Power Control

This simulation is derived from 3GPP TS36.213 PUSCH Power Control algorithm (which is based on P0). In addition to that, the PUSCH TX power effect is also being studied when UL SINR is taken into account in PUSCH TX power adjustment algorithm.

### Calculation

The calculation for this simulation is taken straight from the 3GPP TS36.213 Power Control (for P0-Based PUSCH Power Control).
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-UL-Power-Control/blob/master/img/PUSCH_Formula.png" alt="PUSCH P0 Based Formula" title="PUSCH P0 Based Formula" width=100% height=100% />
<br />
<br />
In 3GPP, only P0-Based PUSCH Power Control algorithm is being specified. To further enhance close loop power control based on UL SINR, few more calculations need to be made.

    1. UL Rx Power = UL Tx Power - UL Path Loss
    2. UL SINR = UL Rx Power / UL RSSI 

### Assumptions

Assumptions need to be made to cover the whole spectrum of simulations. Below are some assumptions needed, some of them will be prompt for input while running the code.

    1. Maximum UE Allowable TX Power - To know the limitation of the UE TX power
    2. Cell RS Power - To estimate UL path loss
    3. Total PRB - To limit simulation up to desired spectrum bandwidth
    4. UL RSSI - To understand noise condition for UL at the required simulation time
    5. UL SINR Target - To simulate TX power compensation needed to achieve UL required SINR (SINR-Based PUSCH Power Control)  

### Results

The impact of TX power change in P0-Based PUSCH Power Control when alpha and P0 parameter settings is being changed:
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-UL-Power-Control/blob/master/img/Result_PUSCH_alpha%2BP0_P0Based.png" alt="alpha & p0" title="alpha & p0" width=100% height=100% />
<br />
<br />
The impact of TX power change in P0-Based PUSCH Power Control when different number of UL PRB is being scheduled. The result also try to consider enhancement of the feature by taking UL SINR into account for PUSCH TX power compensation (SINR-Based PUSCH Power Control).
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-UL-Power-Control/blob/master/img/Result_PUSCH_PRB_P0%2BSINRBased.png" alt="PRB p0 vs SINR" title="PRB p0 vs SINR" width=100% height=100% />
<br />
<br />

