import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GoogleSignin.settings')
import csv
import django
django.setup()


from GoogleSignInApp.models import *

#Reading and populating data to mysql db

with open('GoogleSignInApp/DataForRoche/PivotTable.csv', 'r') as csvfile:
	Data = csv.DictReader(csvfile)
	for row in Data:
		Pivot_table_obj = Pivot_table(ProductName=row['ProductName'])
		Pivot_table_obj.PO_Crearte_to_Release = row['AVERAGE of PO Crearte to Release']
		Pivot_table_obj.Pkg_Start_to_Finish = row['AVERAGE of Pkg Start to Finish']
		Pivot_table_obj.Release_to_Pkg_Start = row['AVERAGE of Release to Pkg Start']
		Pivot_table_obj.BRR_Start_To_Finish = row['AVERAGE of BRR Start To Finish']
		Pivot_table_obj.BRR_Finish_to_QP_Release = row['AVERAGE of BRR Finish to QP Release']
		Pivot_table_obj.save()
		print(Pivot_table_obj)