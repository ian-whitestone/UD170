import csv
import seaborn as sns


def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


def seaborn_plot(df,plot_type='pairplot',columns=False):
	sns.set()
	mpl.rc("figure", figsize=(16, 8.65))
	plotting_df=(df[columns] if columns else df)
	if plot_type=='pairplot':
		sns.pairplot(plotting_df)
	elif plot_type=='corr_plot':
		sns.corrplot(plotting_df)
	sns.plt.show()
	return

