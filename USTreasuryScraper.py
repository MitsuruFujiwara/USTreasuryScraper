import pandas as pd
import numpy as np

class USTScraper(object):

    """
    A class for generating historical dataset of US Treasury yield.
    The data is downloaded from fed's web site.
    https://www.federalreserve.gov/
    """

    def __init__(self):
        self.url='https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=bf17364827e38702b42a58cf8eaa3f78&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package'
        self.columns=['date', 'UST_1M', 'UST_3M', 'UST_6M', 'UST_1Y', 'UST_2Y', \
        'UST_3Y', 'UST_5Y', 'UST_7Y', 'UST_10Y', 'UST_20Y', 'UST_30Y']

    def getData(self):
        # download csv file
        df = pd.read_csv(self.url)

        # set columns
        df.columns = self.columns

        # delete blank
        df = df[5:]

        # set index
        df.index = pd.to_datetime(df['date'])
        df = df.drop('date', axis=1)

        # drop NA
        df = df.replace('ND',np.nan)
        df = df.dropna()

        # set datatype as float
        df= df.astype(float)
        return df

if __name__ == '__main__':
    # test
    ust = USTScraper()
    df = ust.getData()
    print(df)
