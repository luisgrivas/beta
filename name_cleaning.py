
import correction as cr
import pandas as pd 

titles = ['LIC ', 'LIC\.', 'DR ', 'DR\.', 'MC ', 'MC\.', 'M\.C\.', 'ING ', 'ING\.']
latin_characters = [('Á', 'A'), ('É', 'E'), ('Í', 'I'), ('Ó', 'O'), ('Ú', 'U'), ('Ñ', 'N')]


def clean(column):
	column = column.fillna('')
	
	for latin in latin_characters:
		column = (column.str.upper()
                  .str.replace(latin[0], latin[1]))

	for title in titles:
		column = (column.str.replace(title, '')
			.str.strip())

	return column

def split_names(column):
    df_column = column.str.split(' ', expand=True)
    return df_column 	

def paste_name(*args):
	if len(args) == 1:
		return args
	else:
		tmp = (args[0].str.cat(list(args[1]), sep='_')
		.str.rstrip('_')
		.str.lstrip('_'))
	if len(args) > 2: 
		tmp = (tmp.str.cat(list(arg), sep='_')
			.str.rstrip('_')
			.str.lstrip('_'))
	return tmp 