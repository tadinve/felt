
from django.http import HttpResponse
from django.db.models import *
from django.db import connection
from roche_app.models import *
from django.db.models import Q
import collections


def GetDataForChart():
	str1 = 'select product, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel group by product;'
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	#print(lis[0])
	return lis

def GetMinMaxDateFromDatabase():
	format = "%d-%M-%Y"
	str1 = "select min(str_to_date(process_order_creation_date,'"+format+"')),max(str_to_date(process_order_creation_date,'"+format+"')) from roche_app_rochenewmodel"
	row = GetDataFromDatabase(str1)
	return row

def GetAllProducts():
	rows = GetDataFromDatabase('select Distinct(product) from roche_app_rochenewmodel;')
	RocheProductList = list()
	for row in rows:
		RocheProductList.append(row[0])
	return RocheProductList

def GetDataFromDatabase(str1):
	lis = []
	c = connection.cursor()
	c.execute(str1)
	rows = c.fetchall()
	for row in rows:	
		lis.append(row)
	return lis

def GetProductName(product):
	str1 = 'select product_name from roche_app_rochenewmodel where product = "'+ product +'" group by product_name;'
	rows = GetDataFromDatabase(str1)
	return rows

def GetBatchNumber(product_name):
	str1 = 'select batch_number from roche_app_rochenewmodel where product_name = "'+ product_name +'" group by batch_number;'
	#print(str1)
	rows = GetDataFromDatabase(str1)
	return rows

def GetChartForProductName(product,fd,td):
	print(product,fd,td)
	format = "%d-%M-%Y"
	str1=str()
	if product == "All" or product == "all":
		str1 = "select product, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where str_to_date(process_order_creation_date,'"+format+"') Between '"+fd+"' and '"+td+"' group by product;"
	else:
		str1 = "select product_name, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where str_to_date(process_order_creation_date,'"+format+"') Between '"+fd+"' and '"+td+"' and product = '"+product+"' group by product_name;"
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	return lis

def GetChartForBatchNumber(product,product_name,fd,td):
	format = "%d-%M-%Y"
	str1=str()
	if product_name == "All" or product_name == "all":
		str1 = 'select product_name, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where product = "'+ product +'" and str_to_date(process_order_creation_date,"'+format+'") Between "'+fd+'" and "'+td+'"  group by product_name;'
	else:
		str1 = 'select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where product_name = "'+ product_name +'" and str_to_date(process_order_creation_date,"'+format+'") Between "'+fd+'" and "'+td+'" group by batch_number;'
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	return lis

def GetChartForBatchNumberFinal(product,product_name,batch_number,fd,td):
	format = "%d-%M-%Y"
	str1=str()
	if batch_number == "All" or product_name == "all" or batch_number == "All":
		str1 = 'select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where product_name = "'+ product_name +'" and and str_to_date(process_order_creation_date,"'+format+'") Between "'+fd+'" and "'+td+'" group by batch_number;'
	else:
		str1 = 'select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where product_name = "'+ product_name +'" and batch_number = "'+ batch_number +'" and str_to_date(process_order_creation_date,"'+format+'") Between "'+fd+'" and "'+td+'";'
		#print(str1)
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	return lis

def GetBrrReport():
	str1 = "select process_order_number,material_number,product_name,batch_number,packaging_final_check_date,batch_status from roche_app_rochenewmodel LIMIT 100;"
	row = GetDataFromDatabase(str1)
	return row

def GetChartFromDateAndTo(p,pn,bn,fd,td):
	format = "%d-%M-%Y"
	str1 = str()
	print(p,pn,bn,fd,td)
	if (p == "all" or p == "All"):
		str1 = "select product, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where str_to_date(process_order_creation_date,'"+format+"') Between '"+fd+"' and '"+td+"' group by product;"
	elif (p != "all" or p != "All") and (pn == "All" or pn == "all") :
		str1 = "select product_name, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where str_to_date(process_order_creation_date,'"+format+"') Between '"+fd+"' and '"+td+"' and product = '"+p+"' group by product_name;"
	elif (pn != "all" or p != "All") and (bn == "all" or bn == "ALl"):
		str1 = "select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where str_to_date(process_order_creation_date,'"+format+"') Between '"+fd+"' and '"+td+"' and product_name = '"+pn+"' group by batch_number;"
	elif (bn != "all" or bn !="All"):
		str1 = "select batch_number, avg(po_create_to_po_release), avg(po_release_to_pkg_start), avg(pkg_start_to_pkg_finish), avg(pkg_finish_to_pkg_final_check), avg(pkg_final_check_to_brr_begin), avg(brr_begin_to_brr_finish), avg(brr_finish_to_qp_release) from roche_app_rochenewmodel where str_to_date(process_order_creation_date,'"+format+"') Between '"+fd+"' and '"+td+"' and batch_number = '"+bn+"';"
	rows = GetDataFromDatabase(str1)
	lis=list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7])])
	return lis
