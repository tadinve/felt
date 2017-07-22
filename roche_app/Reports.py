
from django.http import HttpResponse
from django.db.models import *
from django.db import connection
from roche_app.models import *
from django.db.models import Q
import collections


def GetDataForChart():
	str1 = 'select product, avg(po_create_release), avg(release_to_pkg_start), avg(pkg_start_bbr_finish), avg(pkg_finish_begin), avg(brr_start_finish), avg(brr_finish_qp_release) from roche group by product;'
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6])])
	#print(lis[0])
	return lis

def GetAllProducts():
	rows = GetDataFromDatabase('select Distinct(product) from roche;')
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
	str1 = 'select product_name from roche where product = "'+ product +'" group by product_name;'
	rows = GetDataFromDatabase(str1)
	return rows

def GetBatchNumber(product_name):
	str1 = 'select batch_number from roche where product_name = "'+ product_name +'" group by batch_number;'
	#print(str1)
	rows = GetDataFromDatabase(str1)
	return rows

def GetChartForProductName(product):
	if product == "All" or product == "all":
		str1 = 'select product, avg(po_create_release), avg(release_to_pkg_start), avg(pkg_start_bbr_finish), avg(pkg_finish_begin), avg(brr_start_finish), avg(brr_finish_qp_release) from roche group by product;'
	else:
		str1 = 'select product_name, avg(po_create_release), avg(release_to_pkg_start), avg(pkg_start_bbr_finish), avg(pkg_finish_begin), avg(brr_start_finish), avg(brr_finish_qp_release) from roche where product = "'+ product +'" group by product_name;'
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6])])
	return lis

def GetChartForBatchNumber(product,product_name):
	if product_name == "All" or product_name == "all":
		str1 = 'select product_name, avg(po_create_release), avg(release_to_pkg_start), avg(pkg_start_bbr_finish), avg(pkg_finish_begin), avg(brr_start_finish), avg(brr_finish_qp_release) from roche where product = "'+ product +'" group by product_name;'
	else:
		str1 = 'select batch_number, avg(po_create_release), avg(release_to_pkg_start), avg(pkg_start_bbr_finish), avg(pkg_finish_begin), avg(brr_start_finish), avg(brr_finish_qp_release) from roche where product_name = "'+ product_name +'" group by batch_number;'
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6])])
	return lis

def GetChartForBatchNumberFinal(product,product_name,batch_number):
	if batch_number == "All" or product_name == "all":
		str1 = 'select batch_number, avg(po_create_release), avg(release_to_pkg_start), avg(pkg_start_bbr_finish), avg(pkg_finish_begin), avg(brr_start_finish), avg(brr_finish_qp_release) from roche where product_name = "'+ product_name +'" group by batch_number;'
	else:
		str1 = 'select batch_number, avg(po_create_release), avg(release_to_pkg_start), avg(pkg_start_bbr_finish), avg(pkg_finish_begin), avg(brr_start_finish), avg(brr_finish_qp_release) from roche where product_name = "'+ product_name +'" and batch_number = "'+ batch_number +'";'
		#print(str1)
	rows = GetDataFromDatabase(str1)
	lis = list()
	for row in rows:
		lis.append([row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6])])
	return lis
