
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
	return rows