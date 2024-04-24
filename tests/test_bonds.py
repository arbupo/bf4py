def generate_plot(data):
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    df = df.sort_values(by='date')    
    df.plot(y='close')
    plt.xlabel('date')
    plt.ylabel('Close Price')
    plt.title('Bond price')

    # Save the plot as a PNG file
    plt.savefig('sample_plot.png')

from bf4py import BF4Py
from datetime import date

isin = 'US912810SN90'
mic = 'XFRA'

bf4py = BF4Py(default_isin=isin,default_mic=mic) 
bond_information = bf4py.bonds.bond_data()
bond_data = bf4py.general.eod_data(min_date=date(2018,1,1))

generate_plot(bond_data)
