
from django.http import HttpResponse
from django.db.models import *
from django.db import connection
from roche_app.models import *
from django.db.models import Q
import collections, csv
import pandas as pd
#import matplotlib.pyplot as plt


def GetDataForChart(): #Fucntion to fetch data for Default Stacked bar charts.
	str1 = 'select product, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel group by product;'
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	#print(lis[0])
	return lis

def GetMinMaxDateFromDatabase(): #Fucntion for getting minimum and maximum date for filter.
	format = "%Y-%m-%d"
	str1 = "select date_format(min(process_order_creation_date),'"+format+"'),date_format(max(process_order_creation_date),'"+format+"') from roche_app_rochenewmodel"
	row = GetDataFromDatabase(str1)
	return row

def GetAllProducts(): #function for getting all the product for filter.
	rows = GetDataFromDatabase('select Distinct(product) from roche_app_rochenewmodel;')
	RocheProductList = list()
	for row in rows:
		RocheProductList.append(row[0])
	return RocheProductList

def GetDataFromDatabase(str1): # Common function for getting data using queries passed from database.
	lis = []
	c = connection.cursor()
	c.execute(str1)
	rows = c.fetchall()
	for row in rows:	
		lis.append(row)
	return lis

def GetProductName(product): #function for getting all the product name for a particular product for filter.
	str1 = 'select product_name from roche_app_rochenewmodel where product = "'+ product +'" group by product_name;'
	rows = GetDataFromDatabase(str1)
	return rows

def GetBatchNumber(product_name):# function for getting all the batch number for a particular product name filter.
	str1 = 'select batch_number from roche_app_rochenewmodel where product_name = "'+ product_name +'" group by batch_number;'
	#print(str1)
	rows = GetDataFromDatabase(str1)
	return rows

def GetChartForProductName(product,fd,td): #Function for getting data for stacked bar chart for all product name of a product.
	print(product,fd,td)
	format = "%d-%M-%Y"
	str1=str()
	if product == "All" or product == "all":
		str1 = "select product, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' group by product;"
	else:
		str1 = "select product_name, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product = '"+product+"' group by product_name;"
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	return lis

def GetChartForBatchNumber(product,product_name,fd,td):#Function for getting data for stacked bar chart for all batch number of a particular product name.
	format = "%d-%M-%Y"
	str1=str()
	if product_name == "All" or product_name == "all":
		str1 = 'select product_name, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where product = "'+ product +'" and process_order_creation_date Between "'+fd+'" and "'+td+'"  group by product_name;'
	else:
		str1 = 'select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where product_name = "'+ product_name +'" and process_order_creation_date Between "'+fd+'" and "'+td+'" group by batch_number;'
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	return lis

def GetChartForBatchNumberFinal(product,product_name,batch_number,fd,td): # function for getting data for stacked bar chart for single bacth number.
	format = "%d-%M-%Y"
	str1=str()
	if batch_number == "All" or product_name == "all" or batch_number == "All":
		str1 = 'select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where product_name = "'+ product_name +'" and process_order_creation_date Between "'+fd+'" and "'+td+'" group by batch_number;'
	else:
		str1 = 'select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where product_name = "'+ product_name +'" and batch_number = "'+ batch_number +'" and process_order_creation_date Between "'+fd+'" and "'+td+'";'
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	return lis

def GetBrrReport(): #function for getting data for BRR report.
	'''str1 = "select process_order_number,material_number,product_name,batch_number,packaging_final_check_date,batch_status, NULL,NULL,NULL,NULL,NULL,NULL from roche_app_rochenewmodel LIMIT 100;"
	row = GetDataFromDatabase(str1)'''
	li=list()
	with open('Upload/BrrPriorityReport2.csv') as file:
		datafile = csv.DictReader(file)
		for row in datafile:
			li.append(row)
	return li

def GetChartFromDateAndTo(p,pn,bn,fd,td): # Fcuntion for getting data based on date filter
	format = "%d-%M-%Y"
	str1 = str()
	print(p,pn,bn,fd,td)
	if (p == "all" or p == "All"):
		str1 = "select product, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' group by product;"
	elif (p != "all" or p != "All") and (pn == "All" or pn == "all") :
		str1 = "select product_name, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product = '"+p+"' group by product_name;"
	elif (pn != "all" or p != "All") and (bn == "all" or bn == "ALl"):
		str1 = "select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product_name = '"+pn+"' group by batch_number;"
	elif (bn != "all" or bn !="All"):
		str1 = "select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and batch_number = '"+bn+"';"
	rows = GetDataFromDatabase(str1)
	lis=list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	return lis


def GetBoxPlotChart(p,pn,bn,fd,td,process_name):# fucntion to getting data for box plot chart according to filters.
	format = "%d-%M-%Y"
	str1 = str()
	rows = []
	dict3 = {'PO Create to PO Release':'po_create_to_po_release', 'PO Release to Pkg Start':' po_release_to_pkg_start', 'Pkg Start to Pkg Finish':'pkg_start_to_pkg_finish', 'Pkg Finish to Pkg Final Check': 'pkg_finish_to_pkg_final_check','Pkg Final Check to BRR Begin':'pkg_final_check_to_brr_begin','BRR Begin To BRR Finish': 'brr_begin_to_brr_finish', 'BRR Finish to QP Release':'brr_finish_to_qp_release' }
	if process_name == 'End to End':
		rows = getDataForEndToEndForBoxPlot(p,pn,bn,fd,td,process_name)
	elif (p == "all" or p == "All"):
		str1 = "select product,"+dict3[process_name]+" from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"';"
		rows = GetDataFromDatabase(str1)
	elif (p != "all" or p != "All") and (pn == "All" or pn == "all" or pn == "") :
		str1 = "select product_name, "+dict3[process_name]+" from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product = '"+p+"' ;"
		rows = GetDataFromDatabase(str1)
	elif (pn != "all" or p != "All") and (bn == "all" or bn == "All"):
		str1 = "select batch_number, "+dict3[process_name]+" from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product_name = '"+pn+"';"
		rows = GetDataFromDatabase(str1)
	elif (bn != "all" or bn !="All"):
		str1 = "select batch_number, "+dict3[process_name]+" from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and batch_number = '"+bn+"' ;"
		rows = GetDataFromDatabase(str1)
	lis=list()
	dict2 = {}
	boxPlot = []
	uniq_elements = dict((x[0],[]) for x in rows)
	for row in rows:
		uniq_elements[row[0]].append(float(row[1])) # arrange the scattered data into proper format for passing it into pandas.
	for element,values in uniq_elements.items():
		df = pd.Series(values)
		#print(df)
		boxPlot.append({'element': element, 'min':float(df.min() if df.min() != 0 else 0),'max':float(df.max() if df.max() !=0 else 0),'median':float(df.median() if df.median() !=0 else 0),'Q1':int(df.quantile(.25) if df.quantile(.25) !=0 else 0),'Q3':int(df.quantile(.75) if df.quantile(.75) !=0 else 0)}) # using pandas for manipulating data.
	return boxPlot

def getDataForEndToEndForBoxPlot(p,pn,bn,fd,td,process_name): # fcuntion to get data when there is  "ENd to End" selected in the filter.
	format = "%d-%M-%Y"
	str1 = str()
	dict3 = {'PO Create to PO Release':'po_create_to_po_release', 'PO Release to Pkg Start':' po_release_to_pkg_start', 'Pkg Start to Pkg Finish':'pkg_start_to_pkg_finish', 'Pkg Finish to Pkg Final Check': 'pkg_finish_to_pkg_final_check','Pkg Final Check to BRR Begin':'pkg_final_check_to_brr_begin','BRR Begin To BRR Finish': 'brr_begin_to_brr_finish', 'BRR Finish to QP Release':'brr_finish_to_qp_release' }
	if (p == "all" or p == "All"):
		str1 = "select product,(po_create_to_po_release + po_release_to_pkg_start + pkg_start_to_pkg_finish + pkg_finish_to_pkg_final_check + pkg_final_check_to_brr_begin + brr_begin_to_brr_finish + brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"';"
	elif (p != "all" or p != "All") and (pn == "All" or pn == "all" or pn == "") :
		str1 = "select product_name, (po_create_to_po_release + po_release_to_pkg_start + pkg_start_to_pkg_finish + pkg_finish_to_pkg_final_check + pkg_final_check_to_brr_begin + brr_begin_to_brr_finish + brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product = '"+p+"' ;"
	elif (pn != "all" or p != "All") and (bn == "all" or bn == "All"):
		str1 = "select batch_number, (po_create_to_po_release + po_release_to_pkg_start + pkg_start_to_pkg_finish + pkg_finish_to_pkg_final_check + pkg_final_check_to_brr_begin + brr_begin_to_brr_finish + brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product_name = '"+pn+"';"
	elif (bn != "all" or bn !="All"):
		str1 = "select batch_number, (po_create_to_po_release + po_release_to_pkg_start + pkg_start_to_pkg_finish + pkg_finish_to_pkg_final_check + pkg_final_check_to_brr_begin + brr_begin_to_brr_finish + brr_finish_to_qp_release) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and batch_number = '"+bn+"' ;"
	rows = GetDataFromDatabase(str1)
	return rows

def GetLineChartDetails(p,pn,bn,fd,td,process_name): #function to get data for line chart according to all filters.
	format = "%d-%M-%Y"
	format2 = "%Y-%m"
	str1 = str()
	rows = []
	dict3 = {'PO Create to PO Release':'po_create_to_po_release', 'PO Release to Pkg Start':' po_release_to_pkg_start', 'Pkg Start to Pkg Finish':'pkg_start_to_pkg_finish', 'Pkg Finish to Pkg Final Check': 'pkg_finish_to_pkg_final_check','Pkg Final Check to BRR Begin':'pkg_final_check_to_brr_begin','BRR Begin To BRR Finish': 'brr_begin_to_brr_finish', 'BRR Finish to QP Release':'brr_finish_to_qp_release' }
	if process_name == 'End to End':
		rows = getDataForEndToEndForLineChart(p,pn,bn,fd,td)
	elif (p == "all" or p == "All"):
		str1 = "select date_format(process_order_creation_date,'"+format2+"') as mon, avg("+dict3[process_name]+") from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' group by mon;"
		rows = GetDataFromDatabase(str1)
	elif (p != "all" or p != "All") and (pn == "All" or pn == "all" or pn == "") :
		str1 = "select date_format(process_order_creation_date,'"+format2+"') as mon, avg("+dict3[process_name]+") from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product = '"+p+"' group by mon;"
		rows = GetDataFromDatabase(str1)
	elif (pn != "all" or p != "All") and (bn == "all" or bn == "All"):
		str1 = str1 = "select date_format(process_order_creation_date,'"+format2+"') as mon, avg("+dict3[process_name]+") from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product_name = '"+pn+"' group by mon;"
		rows = GetDataFromDatabase(str1)
	elif (bn != "all" or bn !="All"):
		str1 = str1 = "select date_format(process_order_creation_date,'"+format2+"') as mon, avg("+dict3[process_name]+") from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and batch_number = '"+bn+"' group by mon;"
		rows = GetDataFromDatabase(str1)
	lis=list()
	for row in rows:
		lis.append([row[0],float(row[1])])
	return lis


def getDataForEndToEndForLineChart(p,pn,bn,fd,td): #fcuntion to get data when there is  "ENd to End" selected in the filter.
	format = "%d-%M-%Y"
	format2 = "%Y-%m"
	str1 = str()
	dict3 = {'PO Create to PO Release':'po_create_to_po_release', 'PO Release to Pkg Start':' po_release_to_pkg_start', 'Pkg Start to Pkg Finish':'pkg_start_to_pkg_finish', 'Pkg Finish to Pkg Final Check': 'pkg_finish_to_pkg_final_check','Pkg Final Check to BRR Begin':'pkg_final_check_to_brr_begin','BRR Begin To BRR Finish': 'brr_begin_to_brr_finish', 'BRR Finish to QP Release':'brr_finish_to_qp_release' }
	if (p == "all" or p == "All"):
		str1 = "select date_format(process_order_creation_date,'"+format2+"') as mon, (avg(po_create_to_po_release) + avg(po_release_to_pkg_start) + avg(pkg_start_to_pkg_finish) + avg(pkg_finish_to_pkg_final_check) + avg(pkg_final_check_to_brr_begin) + avg(brr_begin_to_brr_finish) + avg(brr_finish_to_qp_release)) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' group by mon;"
	elif (p != "all" or p != "All") and (pn == "All" or pn == "all" or pn == ""):
		str1 = "select date_format(process_order_creation_date,'"+format2+"') as mon, (avg(po_create_to_po_release) + avg(po_release_to_pkg_start) + avg(pkg_start_to_pkg_finish) + avg(pkg_finish_to_pkg_final_check) + avg(pkg_final_check_to_brr_begin) + avg(brr_begin_to_brr_finish) + avg(brr_finish_to_qp_release)) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product = '"+p+"' group by mon;"
	elif (pn != "all" or p != "All") and (bn == "all" or bn == "All"):
		str1 = "select date_format(process_order_creation_date,'"+format2+"') as mon, (avg(po_create_to_po_release) + avg(po_release_to_pkg_start) + avg(pkg_start_to_pkg_finish) + avg(pkg_finish_to_pkg_final_check) + avg(pkg_final_check_to_brr_begin) + avg(brr_begin_to_brr_finish) + avg(brr_finish_to_qp_release)) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product_name = '"+pn+"' group by mon;"
	elif (bn != "all" or bn !="All"):
		str1 = "select date_format(process_order_creation_date,'"+format2+"') as mon, (avg(po_create_to_po_release) + avg(po_release_to_pkg_start) + avg(pkg_start_to_pkg_finish) + avg(pkg_finish_to_pkg_final_check) + avg(pkg_final_check_to_brr_begin) + avg(brr_begin_to_brr_finish) + avg(brr_finish_to_qp_release)) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and batch_number = '"+bn+"' group by mon;"
	print(str1)
	rows = GetDataFromDatabase(str1)
	return rows

def GetPAPLQP(p,pn,bn,fd,td):
	format = "%d-%M-%Y"
	str1 = str()
	print(p,pn,bn,fd,td)
	if (p == "all" or p == "All"):
		str1 = "select product, avg(PL), avg(PA), avg(QA) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' group by product;"
	elif (p != "all" or p != "All") and (pn == "All" or pn == "all" or pn == "") :
		str1 = "select product_name, avg(PL), avg(PA), avg(QA) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product = '"+p+"' group by product_name;"
	elif (pn != "all" or p != "All") and (bn == "all" or bn == "All"):
		str1 = "select batch_number, avg(PL), avg(PA), avg(QA) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and product_name = '"+pn+"' group by batch_number;"
	elif (bn != "all" or bn !="All"):
		str1 = "select batch_number, avg(PL), avg(PA), avg(QA) from roche_app_rochenewmodel where process_order_creation_date Between '"+fd+"' and '"+td+"' and batch_number = '"+bn+"';"
	print(str1)
	rows = GetDataFromDatabase(str1)
	lis=list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3])])
	return lis

def GetPAPLQPPercentage(PA,PL,QA,EE):
	datasql = "select PL,PA,QA,EE from roche_app_rochenewmodel;"
	data = GetDataFromDatabase(datasql)
	df = pd.DataFrame(data, columns=["PL","PA","QA","EE"])
	#print(PA,PL,QA,EE)
	count = df.count()
	#print(df[df['PL'] < int(PL)])
	PAp = df[df['PA'] < int(PA)].count() / count['PA'] * 100
	QAp = df[df['QA'] < int(QA)].count() / count['QA'] * 100
	PLp = df[df['PL'] < int(PL)].count() / count['PL'] * 100
	EEp = df[df['EE'] < int(EE)].count() / count['EE'] * 100
	#print(PAp['PA'],QAp['QA'],PLp['PL'])
	lis = [['PA',int(PAp['PA'])],['QA',int(QAp['QA'])],['PL',int(PLp['PL'])],['EE',int(EEp['EE'])]]
	return lis

def YieldPlant():
	plantname = "select distinct(Plant_Name) from YieldDB;"
	data = GetDataFromDatabase(plantname)
	format = "%Y-%m-%d"
	str1 = "select date_format(min(Actual_finish),'"+format+"'),date_format(max(Actual_finish),'"+format+"') from YieldDB;"
	date = GetDataFromDatabase(str1)
	lis = [data,[str(date[0][0]),str(date[0][1])]]
	print(lis)
	return lis

def GetYieldProduct(plant):
	rows = GetDataFromDatabase('select Distinct(Product_Family) from YieldDB where Plant_Name = "'+plant+'"')
	RocheProductList = list()
	for row in rows:
		RocheProductList.append(row[0])
	return RocheProductList

def GetYieldProductName(plant,product):
	rows = GetDataFromDatabase('select Distinct(Product_Name) from YieldDB where Plant_Name = "'+plant+'" and Product_Family = "'+product+'"')
	RocheProductList = list()
	for row in rows:
		RocheProductList.append(row[0])
	return RocheProductList

def YieldProductNameDetails(plant,product,product_name):
	rows = GetDataFromDatabase('select Distinct(Batch) from YieldDB where Plant_Name = "'+plant+'" and Product_Family = "'+product+'" and product_Name = "'+product_name+'"')
	RocheProductList = list()
	for row in rows:
		RocheProductList.append(row[0])
	return RocheProductList

def YieldChartDetails(pl,p,pn,bn,fd,td):
	format = "%d-%M-%Y"
	str1 = str()
	print(pl,p,pn,bn,fd,td)
	if (pl == "all" or pl == "All" or pl == ""):
		str1 = "select plant_name, sum($s_lost___Fill), sum($s_lost___Insp), sum($s_lost___Pkg) from YieldDB where Actual_finish Between '"+fd+"' and '"+td+"' group by plant_name;"
	elif (p == "all" or p == "All"):
		str1 = "select Product_Family, sum($s_lost___Fill), sum($s_lost___Insp), sum($s_lost___Pkg)from YieldDB where Actual_finish Between '"+fd+"' and '"+td+"' and plant_Name = '"+pl+"' group by product_family;"
	elif (p != "all" or p != "All") and (pn == "All" or pn == "all" or pn == "") :
		str1 = "select product_name, sum($s_lost___Fill), sum($s_lost___Insp), sum($s_lost___Pkg) from YieldDB where Actual_finish Between '"+fd+"' and '"+td+"' and product_family = '"+p+"' group by product_name;"
	elif (pn != "all" or p != "All") and (bn == "all" or bn == "All"):
		str1 = "select batch, sum($s_lost___Fill), sum($s_lost___Insp), sum($s_lost___Pkg) from YieldDB where Actual_finish Between '"+fd+"' and '"+td+"' and product_name = '"+pn+"' group by batch;"
	elif (bn != "all" or bn !="All"):
		str1 = "select batch, sum($s_lost___Fill), sum($s_lost___Insp), sum($s_lost___Pkg) from YieldDB where Actual_finish Between '"+fd+"' and '"+td+"' and batch = '"+bn+"';"
	#print(str1)
	rows = GetDataFromDatabase(str1)
	lis=list()
	for row in rows:
		lis.append([str(row[0]),float(row[1]),float(row[2]),float(row[3])])
	#print(lis)
	return lis