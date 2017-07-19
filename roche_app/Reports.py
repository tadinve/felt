
from django.http import HttpResponse
from django.db.models import Max, Sum
from django.db import connection
from roche_app.models import *
from django.db.models import Q
import collections


def GetDataForChart():
	str1 = 'select * from GoogleSignInApp_pivot_table'
	MetricData_obj = Pivot_table.objects.raw(str1)
	lis = []
	for row in MetricData_obj:
		lis.append([row.ProductName,row.PO_Crearte_to_Release,row.Pkg_Start_to_Finish,row.Release_to_Pkg_Start,row.BRR_Start_To_Finish,row.BRR_Finish_to_QP_Release])
	return lis
