# Author: Zulfadli Zainal

from cProfile import label
from parameter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create dataframe
def create_dataframe():

    # Create index

    df_prach = pd.DataFrame()
    df_prach.index = list(start_rsrp)

    # Create list from preambleTransMax

    preamble_att = list(range(1, preambleTransMax + 1))

    # Create Column

    i = 1
    for j in range(len(preamble_att)):
        col_name = 'n' + str(i)
        df_prach.loc[:, col_name] = i - 1
        i += 1

    return df_prach


def prach_txpower(df_prach):

    for column in df_prach:
        df_prach[column] = preambleInitialReceivedTargetPower + \
            ((df_prach.index-referenceSignalPower)*(-1)) + \
            (df_prach[column]*powerRampingStep)
        df_prach[column] = np.where(
            df_prach[column] > pmax, pmax, df_prach[column])

    # Duplicate n1 as n0 - Fix for step charts
    n1 = df_prach.iloc[:, 0].copy()
    df_prach.insert(0, 'n0', n1)

    return df_prach


def pusch_msg3_txpower(df_prach):

    df_pusch_msg3 = df_prach.copy()

    for column in df_pusch_msg3:
        df_pusch_msg3[column] = df_pusch_msg3[column] + deltaPreambleMsg3
        df_pusch_msg3[column] = np.where(
            df_pusch_msg3[column] > pmax, pmax, df_pusch_msg3[column])

    return df_pusch_msg3


def plot_prach(df_prach):

    df_prach = df_prach.transpose()

    plt.step(df_prach.index, df_prach)

    plt.title(f'\nPRACH MSG1 TxPower (dBm)\n', fontsize=14)
    plt.ylabel(f'PRACH MSG1 TxPower (dBm)\n', fontsize=12)
    plt.xlabel(f'\nPreamble Trans Count', fontsize=12)

    plt.ylim(pmax-pmax-5, pmax+5)
    plt.xlim(-0.1, preambleTransMax-1)

    # Set x-ticks every 5 steps
    xticks = range(0, preambleTransMax, 2)
    plt.xticks(xticks)

    plt.grid()
    plt.legend(start_rsrp, bbox_to_anchor=(
        1.32, 0.9), title="Start RSRP (dBm)")

    plt.savefig(f'result_prach_txpower.png', dpi=300, bbox_inches='tight')
    plt.show()

    return


def plot_pusch_msg3(df_pusch_msg3):

    df_pusch_msg3 = df_pusch_msg3.transpose()

    plt.step(df_pusch_msg3.index, df_pusch_msg3)

    plt.title(f'\nPUSCH MSG3 TxPower (dBm)\n', fontsize=14)
    plt.ylabel(f'PUSCH MSG3 TxPower (dBm)\n', fontsize=12)
    plt.xlabel(f'\nPreamble Trans Count', fontsize=12)

    plt.ylim(pmax-pmax-5, pmax+5)
    plt.xlim(-0.1, preambleTransMax-1)

    # Set x-ticks every 5 steps
    xticks = range(0, preambleTransMax, 2)
    plt.xticks(xticks)

    plt.grid()
    plt.legend(start_rsrp, bbox_to_anchor=(
        1.32, 0.9), title="Start RSRP (dBm)")

    plt.savefig(f'result_pusch_msg3_txpower.png', dpi=300, bbox_inches='tight')
    plt.show()

    return
