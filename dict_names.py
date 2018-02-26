import csv
import pickle

reader_m = csv.DictReader(open('data/hombres.csv'))
reader_f = csv.DictReader(open('data/mujeres.csv'))
reader_lm = csv.DictReader(open('data/apellidos.csv'))

names = {}
for row in reader_m: 
	key = row.pop('nombre')
	value = int(row.pop('frec'))
	names[key] = value

names2 = {}
for row in reader_f: 
	key = row.pop('nombre')
	value = int(row.pop('frec'))
	names2[key] = value

lastnames = {}
for row in reader_lm: 
	key = row.pop('apellido')
	value = int(row.pop('frec_pri'))
	lastnames[key] = value

names.update(names2)

with open('data/names.pickle', 'wb') as f: 
	pickle.dump(names, f)

with open('data/lastnames.pickle', 'wb') as f: 
	pickle.dump(lastnames, f)
