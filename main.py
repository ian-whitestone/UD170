import general_utils as Ugen
import matplotlib.pyplot as plt
import pandas as pd
import math
from pandas.tools.plotting import scatter_matrix
import numpy as np
from scipy import stats


#turn this into a class...
print ('running')

def get_data(normalize_features):
	#GET DATA
	pitcher_df=pd.read_csv('baseballdata/Pitching.csv') 
	salary_df=pd.read_csv('baseballdata/Salaries.csv') 

	#MERGE AND FILTER DF
	df=pitcher_df.merge(salary_df,'outer',['yearID','playerID','teamID'])
	df=df[df['salary']>0]

	##BUILD ADDITIONAL FEATURES
	df['logsalary']=df.apply(lambda df: math.log10(df['salary']),axis=1)

	for feature in normalize_features:
	    df[feature+'_N']=df.apply(lambda df: df[feature]/df['G'],axis=1)

	##CLEAR NAN'S FROM DF
	df=df.drop(['SH','SF','GIDP','BAOpp'],axis=1) #majority of rows are missing this data so remove first
	df=df.dropna(axis=0)

	return df

def get_corr_dict(df,start_year,end_year):
	corr_dict={}
	for year in range(start_year,end_year):
		corr_dict[year]={}
		year_df=df[df['yearID']==year]
		Y=year_df['logsalary'].values
		year_df=year_df.drop(['logsalary','yearID'],axis=1)
	
		for feature in year_df.keys():
		    corr_dict[year][feature]={}
		    corr_dict[year][feature]['pearsonr']=stats.pearsonr(year_df[feature].values,Y)[0]
		    corr_dict[year][feature]['pval']=stats.pearsonr(year_df[feature].values,Y)[1]
	return corr_dict


def get_ranked_dict(corr_dict): #variables with top 5 correlation
	ranked_dict={}

	for year in corr_dict.keys():
		ranked_dict[year]={}

		keys=list(corr_dict[year].keys())
		vals=[corr_dict[year][key]['pearsonr'] for key in keys]

		i=1
		while i<6: #definitely a better way of doing this..
		    m = max(vals)
		    m_int=[i for i, j in enumerate(vals) if j == m][0]
		    
		    if year==2001:
		    	print (ranked_dict[year].keys())

		    if keys[m_int].split('_')[0] not in list(ranked_dict[year].keys()) and \
		    			keys[m_int].split('_')[0]+'_N' \
		    			not in list(ranked_dict[year].keys()):#don't want to include normalized and 
		        ranked_dict[year][keys[m_int]]={}             #un-normalized feature (essentially double counting) 
		        ranked_dict[year][keys[m_int]]['rank']=i
		        ranked_dict[year][keys[m_int]]['r']=m
		        i+=1
		    del vals[m_int]
		    del keys[m_int]
	return ranked_dict


normalize_features=['BB','HR','H','SO','SHO','W','L','SV','GS','R']
df=get_data(normalize_features)

all_vars=['W','L','G','GS','CG','SHO','SV','IPouts','H','ER','HR',
                 'BB','SO','ERA','IBB','WP','HBP','BK','BFP','GF','R']
feature_vars=[var+'_N' for var in normalize_features]

df=df[all_vars + [var+'_N' for var in normalize_features]+['yearID','logsalary']]

corr_dict=get_corr_dict(df,2000,2015)

ranked_dict=get_ranked_dict(corr_dict)


print ('2014: %s' %ranked_dict[2014])
print ("\n \n")
print ('2001: %s' %ranked_dict[2001])


#Ian:
#next: find a way to graphically show most impt variables over time...



