import general_utils as Ugen



filename='/Users/whitesi/Documents/Programming/Python/Data Analyst ND/UD170/baseballdata/AllstarFull.csv'
# filename='/baseballdata/AllstarFull.csv'


allstarfull=Ugen.read_csv(filename)

if allstarfull:
	print (allstarfull[0])


