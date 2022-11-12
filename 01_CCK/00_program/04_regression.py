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
def save_txt(f,name,path):
	file = open(path+'/'+name+'.txt','a')
	file.write(f)
	file.close()
def save_csv(f,name,path):
	file=open(path+'/'+name+'.csv','a')
	file.write(f)
	file.close()

def std_output(res,name,path):
	df_coef = pd.DataFrame({"params": res.params,  
                        "std err": res.bse,     
                        "t": res.tvalues,
                        "p-values": res.pvalues
                        })
	df_coef.to_csv("%s/%s.csv"%(path,name))

						
path=r'D:\paper_data\01_CCK\02_processed_data'
indices=os.listdir(path)
for indi in indices:
	print(indi)
	id_name=indi.split('_')[1]
	df_id=pd.read_csv('D:\paper_data\\00_indices\\02_processed_data\SWI_indices_%s'%(id_name),encoding='gb18030')
	df_CSAD = pd.read_csv('D:\paper_data\\01_CCK\\02_processed_data\%s'%(indi),encoding='gb18030')

	cols=df_CSAD.shape[1]
	for i in range(2,cols):
		name=df_CSAD.columns[i]
		print(name)
		y=df_CSAD.iloc[0:,i]
		ind=df_id.iloc[0:,i-1]
		ind_abs=df_id.iloc[0:,i-1].abs()
		ind_square=df_id.iloc[0:,i-1].pow(2)
		df=pd.DataFrame()
		df=pd.concat([y,ind,ind_abs,ind_square],axis=1,keys=['y','ind','ind_abs','ind_square'])
		print(df)

		y, X = dmatrices('y ~ ind + ind_abs + ind_square ', data=df, return_type="dataframe")
		model = sm.OLS(y, X)
		res = model.fit()
		result=res.summary().as_text()
		
		if indi=='CSAD_Whole.csv':
			path='D:/paper_data/01_CCK/04_regression/Whole'
			save_txt(result,name,path)
			std_output(res,name,path)
		if indi=='CSAD_Pre.csv':
			path='D:/paper_data/01_CCK/04_regression/Pre'
			save_txt(result,name,path)
			std_output(res,name,path)
		if indi=='CSAD_Post.csv':
			path='D:/paper_data/01_CCK/04_regression/Post'
			save_txt(result,name,path)
			std_output(res,name,path)


