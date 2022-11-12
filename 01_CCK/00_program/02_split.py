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

def get_index(date_t,date):
	rows=df_CSAD.shape[0]
	for i in range(1,rows):
		if date_t.iloc[i][1]==date:
			return i
			
path=r'D:\paper_data\01_CCK\02_processed_data\CSAD_Whole.csv'
df_CSAD = pd.read_csv(path,encoding='gb18030')
i=get_index(df_CSAD,'2020/1/23  ')
print(i)

CSAD_Pre=df_CSAD.iloc[:i+1,1:]
CSAD_Post=df_CSAD.iloc[i+1:,1:]

CSAD_Pre.to_csv(r'D:\paper_data\01_CCK\02_processed_data\CSAD_Pre.csv',encoding='gb18030')
CSAD_Post.to_csv(r'D:\paper_data\01_CCK\02_processed_data\CSAD_Post.csv',encoding='gb18030')

path_2=r'D:\paper_data\00_indices\02_processed_data\SWI_indices_Whole.csv'
df_ind = pd.read_csv(path_2,encoding='gb18030')

ind_Pre=df_ind.iloc[:i+1,1:]
ind_Post=df_ind.iloc[i+1:,1:]
ind_Pre.to_csv(r'D:\paper_data\00_indices\SWI_indices_Pre.csv',encoding='gb18030')
ind_Post.to_csv(r'D:\paper_data\00_indices\SWI_indices_Post.csv',encoding='gb18030')
