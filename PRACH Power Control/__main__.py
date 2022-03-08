# Author: Zulfadli Zainal

from script import *

if __name__ == '__main__':

    df_prach = create_dataframe()

    df_prach = prach_txpower(df_prach)
    df_pusch_msg3 = pusch_msg3_txpower(df_prach)

    plot_prach(df_prach)
    plot_pusch_msg3(df_pusch_msg3)
