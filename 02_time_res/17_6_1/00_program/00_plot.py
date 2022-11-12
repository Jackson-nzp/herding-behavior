import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
import os
import math

path=r'D:\paper_data\02_time_res\\17_6_1\02_processed_data\CSAD_Whole.csv'
df_CSAD =pd.read_csv(path,encoding='gb18030')
cols=df_CSAD.shape[1]
rows=df_CSAD.shape[0]
for i in range(2,cols):
    fig, ax = plt.subplots()
    ax.plot(df_CSAD.iloc[:,1], df_CSAD.iloc[:,i])
    name=df_CSAD.columns[i].rstrip()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(220))
    ax.set(xlabel='date', ylabel='CSADt',
       title='%s'%(name))
    ax.grid()
    fig.savefig("D:\paper_data\\02_time_res\\17_6_1\\06_fig\%s.png"%(name))
