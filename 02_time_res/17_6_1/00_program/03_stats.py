import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
import os
import math

path=r'D:\paper_data\02_time_res\\17_6_1\02_processed_data'
indices=os.listdir(path)

for ind in indices:
	df_CSAD = pd.read_csv(r'D:\paper_data\02_time_res\\17_6_1\02_processed_data\%s'%(ind),encoding='gb18030')
	cols=df_CSAD.shape[1]
	means=[]
	se=[]
	skewness=[]
	kurtosis=[]
	for i in range(2,cols):
		means.append(round(df_CSAD.iloc[1:,i].mean(),5))
		se.append(round(df_CSAD.iloc[1:,i].std(),5))
		skewness.append(round(df_CSAD.iloc[1:,i].skew(),5))
		kurtosis.append(round(df_CSAD.iloc[1:,i].kurtosis(),5))
	means_S=pd.Series(means,name='Means')
	se_S=pd.Series(se,name='St.Dev')
	skew_S=pd.Series(skewness,name='Skew')
	kurt_S=pd.Series(kurtosis,name='Kurt')
	stats=pd.DataFrame()
	ind_name=pd.Series(df_CSAD.columns.values[2:])
	stats=pd.concat([ind_name,means_S,se_S,skew_S,kurt_S],axis=1,keys=['Industry','Means','St.Dev','Skew','Kurt'])

	file_name=ind.split('.')[0]
	
	stats.to_csv(r'D:\paper_data\02_time_res\\17_6_1\03_stats\%s.csv'%(file_name),encoding='gb18030')
