# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def stats_accounts():
    df = pd.read_csv('data_blocks.csv')
    num = len(df.index)
    senders_transacations = df['from_address'].unique()
    receivers_transacations = df['to_address'].unique()
    print(f'The total number of transactions analyzed is {num}.\n'
          f'We found a total of different {senders_transacations.size} senders'
          f' and a total of {receivers_transacations.size} different receivers.\n'
          f'The number of transactions in our model would be {senders_transacations.size+receivers_transacations.size}.')
    return



if __name__ == '__main__':
    stats_accounts()

