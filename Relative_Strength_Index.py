#https://www.macroption.com/rsi-calculation/
#warning: may not work correctly.

from statistics import mean
import ssl
import pandas as pd
ssl._create_default_https_context = ssl._create_unverified_context
def relativeStrength(array):
    xdiff = [array[n]-array[n-1] for n in range(1,len(array))]
    returns=[array_i - xdiff_i for xdiff_i, array_i in zip(xdiff, array)]
    ups_arr=[]
    downs_arr=[]
    for i in returns:
        if i > 0:
           ups_arr.append(i)
        elif i < 0:
            downs_arr.append(i)
    mean_downs=mean(downs_arr[-14:])
    mean_ups=mean(ups_arr[-14:])

    return mean_downs, mean_ups
df=pd.read_csv('https://raw.githubusercontent.com/pytmar/cds_turkey/master/vix-daily_csv%20(1).csv')
relativeStrength(df['VIX Close'].values)
