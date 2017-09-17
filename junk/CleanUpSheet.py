import os, django, csv
import pandas as pd

def CleanUpData():

	with open('RawData.csv', 'r') as csvfile:
		datafile = csv.DictReader(csvfile)
		df = pd.read_csv('RawData.csv')
		print(df.info())
		for row in datafile:
			lis = [row['process_order_number'].lstrip("0"),row['order_type'],row['material_number'].lstrip(0),row['product_name'],row['process_order_creation_date'],row['batch_number'],]
			print(lis)
			'''newFile = open('CleanedDataForRoche.csv', "wb")
			writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
			writer.writerow()'''


if __name__ == '__main__':
	print("Cleaning the data.")
	#populateRocheData()
	CleanUpData()


'''ofile  = open('ttest.csv', "wb")
writer = csv.writer(ofile, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)
 
for row in reader:
	writer.writerow(row)'''