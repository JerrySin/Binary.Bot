import pandas as pd

def printData():
    df = pd.read_csv("Volatility_100_Index_(1t)_20170317_111837.csv")
    print(df)

printData()
