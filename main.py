import general_utils as Ugen
import pandas as pd

#GET DATA
filepath='/Users/whitesi/Documents/Programming/Python/Data Analyst ND/UD170/baseballdata/'
pitchers=Ugen.read_csv(filepath+'Pitching.csv')
salaries=Ugen.read_csv(filepath+'Salaries.csv')

#CLEAN DATA
##Determine which fields you want to be an integer,float,date type or left as a string
float_fields=['ERA','BAOpp']
int_fields=['yearID','stint','W','L','G','GS','CG','SHO','SV','IPOuts','H','ER','HR','BB','SO',
				'IBB','WP','HBP','BK','BFP','GF','R','SH','SF','GIDP']


##Convert the fields
pitchers=Ugen.convert_csv_entries(pitchers,int_fields,float_fields,date_fields=[])
salaries=Ugen.convert_csv_entries(salaries,int_fields=['yearID','salary'],float_fields=[],date_fields=[])


##Add salary data to pitchers table
for pitcher in pitchers:
    for salary in salaries:
        if salary['playerID']==pitcher['playerID'] and salary['yearID']==pitcher['yearID']:
            pitcher['salary']=salary['salary']
            break
        else:
            continue

#Remove pitchers without salary data
pitchers=[player for player in pitchers if 'salary' in player.keys()]
print (len(pitchers))


#Create dataframe
pitchers_df=pd.DataFrame(pitchers)

Ugen.seaborn_plot(pitchers_df,'corr_plot',['salary','yearID'])

