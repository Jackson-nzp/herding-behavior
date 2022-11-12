import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import os
import math
import sys
def float_p(date_t,start_date=2):
	#industry_t stands for the series of all the stock in the industry at day t(list)
	#before entering the number ,make process of it
	#date_t stands for another version of pd
	rows_d=date_t.shape[0]
	cols_d=date_t.shape[1]
	
	date_t_new=pd.DataFrame()
	name=date_t.iloc[1:,1]
	print(name)
	for i in range(0,len(name)):
		number=[]
		for j in range(2,cols_d):
			number.append(float(date_t.iloc[i+1][j]))
		ind=pd.Series(number,name=name[i+1])
		date_t_new['%s'%ind.name]=ind
	return date_t_new
path=r'D:\paper_data\SWI_indices.csv'

df_indices = pd.read_csv(path,encoding='gb18030')

df_indices=float_p(df_indices)

df_indices.to_csv(r'D:\paper_data\SWI_indices_Whole.csv',encoding='gb18030')
