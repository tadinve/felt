from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from roche_app import Reports
from roche_app.models import *
# from django.template.context import RequestContext
from django.http import HttpResponse
from django.template import RequestContext
import json
from django.template.defaulttags import register
from django.core.exceptions import *

def login(request): # Fucntion for handling login requests
	# context = RequestContext(request, {
	#     'request': request, 'user': request.user})
	# return render_to_response('login.html', context_instance=context)
	return render(request, 'login.html')


@login_required(login_url='/')
def home(request): # function for handling request from home tab.
	authenticate = check_for_authentication(request)
	if authenticate:
		lis = Reports.GetDataForChart()
		#print(lis)
		return render_to_response('home.html', {'rdata': json.dumps(lis), 'user': request.user})
	else:
		logout(request)
		return render(HttpResponse("Invalid user"),'login.html')


def logout(request): # Fucntion for handling logout requests
	auth_logout(request)
	return redirect('/')

@login_required(login_url='/')
def BrrPriorityReport(request): #function for handling BRR Report Tab requests
	lis = Reports.GetDataForChart()
	BrrReport=Reports.GetBrrReport()
	#print(BrrReport)
	return render_to_response('BrrPriorityReport.html', {'rdata': json.dumps(lis), 'user': request.user, 'BrrReport': BrrReport})

@login_required(login_url='/')
def dashboard(request): #function for handling Dashboard Tab requests
	authenticate = check_for_authentication(request)
	if authenticate:
		lis = Reports.GetDataForChart()
		RocheObjProduct = Reports.GetAllProducts()
		DateObj = Reports.GetMinMaxDateFromDatabase()
		#print((DateObj[0][0]))
		return render_to_response('dashboard.html',{'rdata': json.dumps(lis),'mindate': DateObj[0][0] ,'maxdate': DateObj[0][1], 'products': RocheObjProduct, 'user': request.user},RequestContext(request))
	else:
		HttpResponse("Invalid user")
		logout(request)
		return render_to_response('login.html')


#@app.route("roche/details/",methods=['GET','POST'])
#@login_required(login_url='/')
def ProductDetails(request): # Function for handling Get request from Dashboard  Product details for filter.
	product = request.GET.get('product_name',None)
	product_names = Reports.GetProductName(product)
	response = HttpResponse(json.dumps(product_names))
	return response

def BatchDetails(request):# Function for handling Get request from Dashboard  Batch details for filter.
	product_name = request.GET.get('product_name',None)
	batch_number = Reports.GetBatchNumber(product_name)
	response = HttpResponse(json.dumps(batch_number))
	return response

def ProductNameChartDetails(request):# Function for handling Get request from Dashboard  Product Name details for stacked bar chart.
	product = request.GET.get('product',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	product_names = Reports.GetChartForProductName(product,from_date,to_date)
	response = HttpResponse(json.dumps(product_names))
	return response

def BatchNumberChartDetails(request):# Function for handling Get request from Dashboard  batch number details for stacked bar chart.
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	batch_number = Reports.GetChartForBatchNumber(product,product_name,from_date,to_date)
	response = HttpResponse(json.dumps(batch_number))
	return response

def check_for_authentication(request):# Function for checking domain name of user's login id to restrict them from un authorised access.
	email = request.user.email
	domain = email.split('@')[1]
	if domain in ['roche.com','solivarlabs.com','contractors.roche.com']:
		return True
	else:
		return False
	'''try:
		authorized_email = UserAuthentication.objects.get(user_id=email)
		if authorized_email.authorized == '1':
			return True
		else:
			return False
	except ObjectDoesNotExist as e:
		return False'''

def BatchNumberChartDetailsFinal(request):# Function for handling Get request from Dashboard  batch number details( Single ) for stacked bar chart.
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch_number = request.GET.get('batch_number',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	#print(product,product_name,batch_number,from_date,to_date)
	batch_number = Reports.GetChartForBatchNumberFinal(product,product_name,batch_number,from_date,to_date)
	response = HttpResponse(json.dumps(batch_number))
	return response

def ChartWithDate(request): # Function for handling Requests from dashboard when date filters are changed.
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch_number = request.GET.get('batch_number',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	data = Reports.GetChartFromDateAndTo(product,product_name,batch_number,from_date,to_date)
	response = HttpResponse(json.dumps(data))
	return response

def BoxPlotChart(request):# Function for handling Requests from dashboard when Box plot filters are applied.
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch_number = request.GET.get('batch_number',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	process_name = request.GET.get('processName',None)
	#print(process_name)
	#print(product,product_name,batch_number,from_date,to_date)
	data = Reports.GetBoxPlotChart(product,product_name,batch_number,from_date,to_date,process_name)
	#print(data)
	#products = Reports.GetAllProducts()
	#print(data)
	response = HttpResponse(json.dumps(data))
	return response

def GetLineChartDetails(request):# Function for handling Requests from dashboard when Line chart filters are applied.
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch_number = request.GET.get('batch_number',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	process_name = request.GET.get('processName',None)
	#print(process_name)
	#print(product,product_name,batch_number,from_date,to_date)
	data = Reports.GetLineChartDetails(product,product_name,batch_number,from_date,to_date,process_name)
	#print(data)
	#products = Reports.GetAllProducts()
	#print(data)
	response = HttpResponse(json.dumps(data))
	return response


@register.filter(name='getkey')
def getkey(value, arg):
    return value[arg]


def GetPAPLQP(request):
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch_number = request.GET.get('batch_number',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	#print(process_name)
	#print(product,product_name,batch_number,from_date,to_date)
	data = Reports.GetPAPLQP(product,product_name,batch_number,from_date,to_date)
	#print(data)
	#products = Reports.GetAllProducts()
	#print(data)
	response = HttpResponse(json.dumps(data))
	return response
	
def GetPAPLQPPercentage(request):
	PA = request.GET.get('PA',None)
	PL = request.GET.get('PL',None)
	QA = request.GET.get('QA',None)
	EE = request.GET.get('EE',None)
	data = Reports.GetPAPLQPPercentage(PA,PL,QA,EE)
	#print(data)
	#products = Reports.GetAllProducts()
	#print(data)
	response = HttpResponse(json.dumps(data))
	return response

def YieldPlant(request):
	data = Reports.YieldPlant()
	response = HttpResponse(json.dumps(data))
	return response

def YieldPlantDetails(request):
	plant = request.GET.get('plant_name',None)
	products = Reports.GetYieldProduct(plant)
	response = HttpResponse(json.dumps(products))
	return response

def YieldProductDetails(request):
	plant = request.GET.get('plant_name',None)
	product = request.GET.get('product',None)
	product_name = Reports.GetYieldProductName(plant,product)
	response = HttpResponse(json.dumps(product_name))
	return response

def YieldProductNameDetails(request):
	plant = request.GET.get('plant_name',None)
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch = Reports.YieldProductNameDetails(plant,product,product_name)
	response = HttpResponse(json.dumps(batch))
	return response

def YieldChartDetails(request):
	plant = request.GET.get('plant_name',None)
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch = request.GET.get('batch_number',None)
	tod = request.GET.get('toDate',None)
	fromd = request.GET.get('fromDate',None)
	data = Reports.YieldChartDetails(plant,product,product_name,batch,fromd,tod)
	response = HttpResponse(json.dumps(data))
	return response


def YieldChartDetailsforKilos(request):
	plant = request.GET.get('plant_name',None)
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch = request.GET.get('batch_number',None)
	tod = request.GET.get('toDate',None)
	fromd = request.GET.get('fromDate',None)
	print(plant,product,product_name,batch,fromd,tod)
	data = Reports.YieldChartDetailsforKilos(plant,product,product_name,batch,fromd,tod)
	response = HttpResponse(json.dumps(data))
	return response
