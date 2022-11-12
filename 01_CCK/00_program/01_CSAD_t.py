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


def date(date_t):
	cols_d=date_t.shape[1]
	date=[]
	for i in range(2,cols_d):
		date.append(date_t.iloc[0][i])#the first row shown in the excel is index of pd,not real data
	return date

def CSAD_t(date_t,start_date=2):
	#industry_t stands for the series of all the stock in the industry at day t(list)
	#before entering the number ,make process of it
	#date_t stands for another version of pd
	rows_d=date_t.shape[0]
	cols_d=date_t.shape[1]
	CSADt=[]
	count=0
	is_null=date_t.isnull()
	for i in range(start_date,cols_d):
		CSAD=0
		for j in range(start_date,rows_d-1):
			'''
			the last row is set for indices,where there should be a alternative solution 
			which in English version
			'''
			if is_null.iloc[j][i]==False:
				CSAD+=abs(float(p_n(date_t.iloc[j][i]))-float(p_n(date_t.iloc[rows_d-1][i])))
				count+=1
		CSAD=CSAD/count
		CSADt.append(CSAD)
	return CSADt

def p_n(s):#a function of processing number
	s=s.replace(',','')
	return s


'''
def transform_return(stock):
	industry_return=pd.DataFrame()
	for item in df_stock.items():#iterring in columns
		data=item[1]#the first is key where the second is data series
		daily_return=pd.Series(data[:2])
		return_list=[]
		for j in range(2,len(data)-1):#the first three lines are index and name of one stock
			return_list.append(math.log(float(p_n(data[j+1]))/float(p_n(data[j])))*100)
		daily_return.append(pd.Series(return_list))
		print(daily_return)
		industry_return = pd.concat([industry_return,daily_return])
	return industry_return
'''

#dealing with missing data
#delete all the NAN data series
path=r'D:\paper_data\01_CCK\01_original_data'
industries=os.listdir(path)

sample=pd.read_csv('D:\paper_data\\01_CCK\\01_original_data\%s'%(industries[0]),encoding='gb18030')

date_S=pd.Series(date(sample),name='Date')

CSAD_W=pd.DataFrame()
CSAD_W[date_S.name]=date_S

for idt in industries:
	df_time = pd.read_csv('D:\paper_data\\01_CCK\\01_original_data\%s'%(idt),encoding='gb18030')
	#df_stock = df_time.T  #column's stock
	
	list_name=idt.split('.')[0]

	CSAD_S=pd.Series(CSAD_t(df_time),name='%s'%list_name)
	CSAD_W[list_name]=CSAD_S
	
	print('Whole:')
	print(CSAD_W)

CSAD_W.to_csv(r'D:\paper_data\01_CCK\02_processed_data\CSAD_Whole.csv',encoding='gb18030')








