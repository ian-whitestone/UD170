import general_utils as Ugen


#GET DATA
filepath='/Users/whitesi/Documents/Programming/Python/Data Analyst ND/UD170/baseballdata/'
pitchers=Ugen.read_csv(filepath+'Pitching.csv')
salaries=Ugen.read_csv(filepath+'Salaries.csv')

#EXPLORE DATA
Ugen.explore_list(pitchers,5) #print first 5 entries
Ugen.explore_list(salaries,5) #print first 5 entries

#CLEAN DATA
##Determine which fields you want to be an integer,float,date type or left as a string
float_fields=['ERA','BAOpp']
int_fields=['yearID','stint','W','L','G','GS','CG','SHO','SV','IPOuts','H','ER','HR','BB','SO',
				'IBB','WP','HBP','BK','BFP','GF','R','SH','SF','GIDP']


##Convert the fields
pitchers=Ugen.convert_csv_entries(pitchers,int_fields,float_fields,date_fields=[])
salaries=Ugen.convert_csv_entries(salaries,int_fields=['yearID'],float_fields=[],date_fields=[])
Ugen.explore_list(pitchers,5) #check converted data


# print (len(pitchers))
# print (len(salaries))
##Lengths are clearly not equal, find out what range of years is covered in each data set



#Need to add salary column/field to pitching table


#Create dataframe




