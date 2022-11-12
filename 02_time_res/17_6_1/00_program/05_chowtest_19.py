from chow_test import chow_test
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
def get_index(date_t,date):
	rows=df_CSAD.shape[0]
	for i in range(1,rows):
		if date_t.iloc[i][1]==date:
			return i

f=open('D:\paper_data\\02_time_res\\17_6_1\\05_chow\chow_19.txt','a')

path=r'D:\paper_data\02_time_res\\17_6_1\02_processed_data\CSAD_Whole.csv'
df_id=pd.read_csv('D:\paper_data\\00_indices\\03_time_res\\17_6_1\SWI_indices_Whole.csv',encoding='gb18030')
df_CSAD = pd.read_csv(path,encoding='gb18030')
i_d=get_index(df_CSAD,'2020/1/23  ')
print(i_d)
cols=df_CSAD.shape[1]
for i in range(2,cols):
    name=df_CSAD.columns[i]
    y=df_CSAD.iloc[0:,i]
    ind=df_id.iloc[0:,i-1]
    ind_abs=df_id.iloc[0:,i-1].abs()
    ind_square=df_id.iloc[0:,i-1].pow(2)
    df=pd.DataFrame()
    df=pd.concat([y,ind,ind_abs,ind_square],axis=1,keys=['y','ind','ind_abs','ind_square'])
    df_2=pd.concat([ind,ind_abs,ind_square],axis=1,keys=['ind','ind_abs','ind_sqaure'])
    y, X = dmatrices('y ~ ind + ind_abs + ind_square ', data=df, return_type="dataframe")
    for i in [0.01,0.05,0.1]:
        res=chow_test(X_series=df_2 ,y_series= df['y'],last_index=i_d,first_index=i_d+1,significance=i)
        print("%s:In the significance level of %f ,the answer is :"%(name,i),file=f,flush=True)
        print(res[0],file=f,flush=True)
        print('F_value:%f\t P_value:%f\n'%(res[1],res[2]),file=f,flush=True)

        print("%s:In the significance level of %f ,the answer is :"%(name,i),file=sys.stdout)
        print(res[0],file=sys.stdout)
        print('\tF_value:%f\t P_value:%f\n'%(res[1],res[2]),file=sys.stdout)

f.close()
