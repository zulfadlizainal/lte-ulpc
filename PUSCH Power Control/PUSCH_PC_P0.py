# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm

# Input Max UE TX Power Capability

max_tx_power = -9999
while 0 > max_tx_power or 30 < max_tx_power:
    try:
        max_tx_power = int(input("Max UE TX Power (dBm): "))
    except ValueError:
        print('Not an Integer')

# Input Cell RS Power per port from SIB2

rs_power = -9999
while 0 > rs_power or 30 < rs_power:
    try:
        rs_power = int(input("Cell RS Power (dBm): "))
    except ValueError:
        print('Not an Integer')

# Input Total PRB for UL

max_ul_prb = -9999
while 0 > max_ul_prb or 100 < max_ul_prb:
    try:
        max_ul_prb = int(input("Max UL PRB: "))
    except ValueError:
        print('Not an Integer')

# Path Loss Range

pl = list(range(80, 161))

# RSRP Range

x = 0
rsrp = [x-rs_power for x in pl]
rsrp = [x*(-1) for x in rsrp]

# Alpha Range

alpha = np.arange(0.1, 1.1, 0.1)
alpha = np.round(alpha, 1)
alpha = alpha.tolist()

# PRB Range

ul_prb = list(range(1, max_ul_prb+1))

# P0 Target Range

p0_nominal_pusch = list(range(-126, -79))
p0_pusch = 0  # Assume

x = 0
p0 = [x+p0_pusch for x in p0_nominal_pusch]

########### Study 1: How much Tx Power is affected by PRB ###########

alpha_param = 1  # Assume
p0_param = -92  # Assume

df_prb = pd.DataFrame({'Path Loss (dB)': pl})
df_prb['RSRP (dBm)'] = (df_prb['Path Loss (dB)'] - rs_power) * -1

index = 0

for index in range(len(ul_prb)):

    df_prb[f'{ul_prb[index]}'] = (
        10*math.log10(ul_prb[index])) + p0_param + (alpha_param*df_prb['Path Loss (dB)'])

df_prb[df_prb > max_tx_power] = max_tx_power

df_prb_plot = df_prb
df_prb_plot = df_prb_plot.drop(['Path Loss (dB)'], axis=1)
df_prb_plot = df_prb_plot.set_index('RSRP (dBm)')

# Plot

xmin = 0
xmax = max_ul_prb
ymin = df_prb.iloc[-1]['RSRP (dBm)']
ymax = df_prb.iloc[0]['RSRP (dBm)']
vmin = -20
vmax = 23

plt.imshow(df_prb_plot, cmap=cm.jet, interpolation='hermite',
           vmin=vmin, vmax=vmax, extent=[xmin, xmax, ymin, ymax])

plt.xlabel("UL Scheduled PRB")
plt.ylabel("RSRP (dBm)")

plt.title(
    f'UL PUSCH TX Power (dBm)\nAssumptions: p0 = {p0_param}dBm, alpha = {alpha_param}\n')
plt.grid(which='major', axis='both', linestyle='--')

plt.colorbar()

plt.show()

########### Study 2: How much Tx Power is affected by alpha ###########

prb_param = 100  # Assume
p0_param = -92  # Assume

df_alpha = pd.DataFrame({'Path Loss (dB)': pl})
df_alpha['RSRP (dBm)'] = (df_alpha['Path Loss (dB)'] - rs_power) * -1

index = 0

for index in range(len(alpha)):

    df_alpha[f'{alpha[index]}'] = (
        10*math.log10(prb_param)) + p0_param + (alpha[index]*df_alpha['Path Loss (dB)'])

df_alpha[df_alpha > max_tx_power] = max_tx_power

df_alpha_plot = df_alpha
df_alpha_plot = df_alpha_plot.drop(['Path Loss (dB)'], axis=1)
df_alpha_plot = df_alpha_plot.set_index('RSRP (dBm)')
df_alpha_plot_filter = df_alpha_plot[df_alpha_plot.columns[-4:]]

# Plot

df_alpha_plot_filter.plot(style='--')

plt.xlabel("RSRP (dBm)")
plt.ylabel("UE TX Power (dBm)")
plt.title(f'UL PUSCH TX Power (dBm)\nAssumptions: UL Scheduled PRB = {prb_param}, p0 = {p0_param}dBm\n')
plt.legend(title='alpha')
plt.grid()

plt.show()

########### Study 3: How much Tx Power is affected by P0 ###########

alpha_param = 1  # Assume
prb_param = 100  # Assume

df_p0 = pd.DataFrame({'Path Loss (dB)': pl})
df_p0['RSRP (dBm)'] = (df_p0['Path Loss (dB)'] - rs_power) * -1

index = 0

for index in range(len(p0)):

    df_p0[f'{p0[index]}'] = (
        10*math.log10(prb_param)) + p0[index] + (alpha_param*df_p0['Path Loss (dB)'])

df_p0[df_p0 > max_tx_power] = max_tx_power

df_p0_plot = df_p0
df_p0_plot = df_p0_plot.drop(['Path Loss (dB)'], axis=1)
df_p0_plot = df_p0_plot.set_index('RSRP (dBm)')

# Plot

xmin = p0[0]
xmax = p0[-1]
ymin = df_p0.iloc[-1]['RSRP (dBm)']
ymax = df_p0.iloc[0]['RSRP (dBm)']
vmin = -20
vmax = 23

plt.imshow(df_p0_plot, cmap=cm.jet, interpolation='hermite',
           vmin=vmin, vmax=vmax, extent=[xmin, xmax, ymin, ymax])

plt.xlabel("p0 (dBm)")
plt.ylabel("RSRP (dBm)")

plt.title(
    f'UL PUSCH TX Power (dBm)\nAssumptions: UL Scheduled PRB = {prb_param}, alpha = {alpha_param}\n')
plt.grid(which='major', axis='both', linestyle='--')

plt.colorbar()

plt.show()
