# PRACH Power Control

This simulation is derived from 3GPP TS36.321 PRACH Power Control algorithm. In addition to that, the PUSCH TX power for MSG3 can also be estimated based on the result refering to TS36.213.

### Calculation

The calculation for PRACH MSG1 Tx Power simulation is taken straight from the 3GPP TS36.321.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-UL-Power-Control/blob/master/img/PRACH_Formula.png" alt="PRACH Formula" title="PRACH Formula" width=100% height=100% />
<br />
<br />

Simplified formula:

    P_PRACH (n1)   = min{P_CMAX, PREAMBLE_RECEIVED_TARGET_POWER + PL}                      (3GPP TS 36.321)
    P_PRACH (>n1) = min{P_CMAX, PREAMBLE_RECEIVED_TARGET_POWER + PL + RAMPINGSTEP}         (3GPP TS 36.321)

Important parameters:

    referenceSignalPower                       # From SIB2 in dBm
    preambleInitialReceivedTargetPower         # From SIB2 in dBm
    powerRampingStep                           # From SIB2 in dB
    preambleTransMax                           # From SIB2 in count
    p-max                                      # From SIB1 in dBm

The calculation for PUSCH MSG3 Tx Power simulation is taken straight from the 3GPP TS36.213.

    P_PUSCH_MSG3 = min{P_CMAX, P_PRACH + (DELTAMSG3)}                                       (3GPP TS 36.213)

Important parameters:

    deltaPreambleMsg3 = 4                      # From SIB2 in dB (IE x 2)

### Assumptions

Below are parameter assumptions taken to produce the results:

    start_rsrp = [-90, -95, -100, -105, -110, -115, -120, -125, -130, -135, -140]
    referenceSignalPower = 20                                                           # From SIB2 in dBm
    preambleInitialReceivedTargetPower = -112                                           # From SIB2 in dBm
    powerRampingStep = 4                                                                # From SIB2 in dB
    preambleTransMax = 10                                                               # From SIB2 in count
    pmax = 23                                                                           # From SIB1 in dBm
    deltaPreambleMsg3 = 4                                                               # From SIB2 in dB (IE x 2)

### Results

Result observed for above parameter set:
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-UL-Power-Control/blob/master/img/Result_PRACH_PowerControl.png" alt="MSG1 & MSG3 Power" title="MSG1 & MSG3 Power" width=100% height=100% />
<br />
<br />

n definitions for MSG3 Power:
n1 = Success MSG2 in n1, start MSG3
n2 = Fail MSG2 in n1, success MSG2 in n2, start MSG3
…
…
n10 = Fail MSG2 in n1 to n9, success MSG2 in n10, start MSG3
