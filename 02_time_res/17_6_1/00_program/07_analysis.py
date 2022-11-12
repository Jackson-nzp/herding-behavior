import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import os
import math
import sys
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols 
from patsy import dmatrices

def p_value(sig_level):
    if sig_level<0.01:
        sig='***'
    elif sig_level<0.05:
        sig='**'
    elif sig_level<0.1:
        sig='*'
    else:
        sig=''
    return sig
path=r'D:\paper_data\02_time_res\\17_6_1\04_regression'
dates=os.listdir(path)
for date in dates:
    path_1='D:\paper_data\\02_time_res\\17_6_1\\04_regression\%s'%(date)
    indices=os.listdir(path_1)
    name_list=[]
    beta_0=[]
    beta_1=[]
    beta_2=[]
    beta_3=[]


    for indi in indices:
        name=indi.split('.')[0]
        file_type=indi.split('.')[1]
        if file_type =='csv':
            name_list.append(name)
            name_list.append('')
            df_coef = pd.read_csv('D:\paper_data\\02_time_res\\17_6_1\\04_regression\%s\%s'%(date,indi))
            b_0='%.5f'%df_coef.iloc[0][1]
            beta_0.append(str(b_0))
            std_0='%.5f'%df_coef.iloc[0][2]
            std='(%s)'%(str(std_0))+p_value(df_coef.iloc[0][4])
            beta_0.append(std)

            b_1='%.5f'%df_coef.iloc[1][1]
            beta_1.append(str(b_1))
            std_1='%.5f'%df_coef.iloc[1][2]
            std='(%s)'%(str(std_1))+p_value(df_coef.iloc[1][4])
            beta_1.append(std)

            b_2='%.5f'%df_coef.iloc[2][1]
            beta_2.append(str(b_2))
            std_2='%.5f'%df_coef.iloc[2][2]
            std='(%s)'%(str(std_2))+p_value(df_coef.iloc[2][4])
            beta_2.append(std)

            b_3='%.5f'%df_coef.iloc[3][1]
            beta_3.append(str(b_3))
            std_3='%.5f'%df_coef.iloc[3][2]
            std='(%s)'%(str(std_3))+p_value(df_coef.iloc[3][4])
            beta_3.append(std)

    analysis=pd.DataFrame({"industry": pd.Series(name_list), 
                        "beta_0": pd.Series(beta_0), 
                        "beta_1": pd.Series(beta_1),
                        "beta_2": pd.Series(beta_2), 
                        "beta_3":pd.Series(beta_3)    
                         })
    analysis.to_csv('D:\paper_data\\02_time_res\\17_6_1\\07_analysis\%s.csv'%date)


