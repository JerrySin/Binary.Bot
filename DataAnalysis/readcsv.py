import pandas as pd
import matplotlib.pyplot as plt

def printData():
    df = pd.read_csv("Volatility 100 Index (1t).csv")
    print df.head(10)

    print "\nMax Index:"
    print get_max_index(df)
    print "\nMin Index:"
    print get_min_index(df)
    print "\nDifference:"
    print get_diff_index(df)
    print "\nMean Index:"
    print get_mean_index(df)

    df['Volatility 100 Index'].plot()
    plt.show()

def get_max_index(df1):
    return df1['Volatility 100 Index'].max()

def get_min_index(df1):
    return df1['Volatility 100 Index'].min()

def get_diff_index(df1):
    return abs(df1['Volatility 100 Index'].max()-df1['Volatility 100 Index'].min())

def get_mean_index(df1):
    return df1['Volatility 100 Index'].mean()

if __name__ == "__main__":
    printData()

# pandas data frame
# .max()
# .min()
# .mean()


# pyp lot
# .xlabel()
# .ylabel()
# 