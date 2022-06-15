import csv
with open(filename, 'r') as f:
	d_reader = csv.DictReader(f, delimiter='\n')
	header = d_reader.fieldnames
	for row in d_reader:
		for head in header:
			print(row[head])
			
