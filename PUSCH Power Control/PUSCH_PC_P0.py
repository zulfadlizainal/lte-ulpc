# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

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

df_prb_plot.plot()

# x = np.arange(len(df_prb_plot.columns))
# y = np.arange(len(df_prb_plot.index))
# X, Y = np.meshgrid(x, y)
# Z = df_prb_plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
#                        linewidth=0, antialiased=False)

# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.title('Original Code')

# ax = plt.gca()
# ax.set_xticks(np.arange(0, max_ul_prb, 10))
# ax.set_yticks(np.arange(-60, -150, 10))

plt.show()


# ######Plot RSRP Map######

# plt.imshow(df_prb_plot, cmap='RdYlGn', interpolation='hermite')

# #plt.colorbar()

# plt.xlabel("Distance (m)")
# plt.ylabel("Distance (m)")

# ax = plt.gca()
# ax.set_xticks(np.arange(grid*(-1), grid, (step*20)))
# ax.set_yticks(np.arange(grid*(-1), grid, (step*20)))

# plt.title("UL PUSCH TX Power (dBm)")
# plt.grid(which='major', axis='both', linestyle='--')

# plt.colorbar()

# plt.show()