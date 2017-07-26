from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from roche_app import Reports
# from django.template.context import RequestContext
from django.http import HttpResponse
from django.template import RequestContext
import json

def login(request):
	# context = RequestContext(request, {
	#     'request': request, 'user': request.user})
	# return render_to_response('login.html', context_instance=context)
	return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
	authenticate = check_for_domain(request)
	if authenticate:
		lis = Reports.GetDataForChart()
		#print(lis)
		return render_to_response('home.html', {'rdata': json.dumps(lis), 'user': request.user})
	else:
		HttpResponse("Invalid user")
		logout(request)
		return render_to_response('login.html')


def logout(request):
	auth_logout(request)
	return redirect('/')

@login_required(login_url='/')
def BrrPriorityReport(request):
	lis = Reports.GetDataForChart()
	BrrReport=Reports.GetBrrReport()
	#print(lis)
	return render_to_response('BrrPriorityReport.html', {'rdata': json.dumps(lis), 'user': request.user, 'BrrReport': BrrReport})

@login_required(login_url='/')
def dashboard(request):
	authenticate = check_for_domain(request)
	if authenticate:
		lis = Reports.GetDataForChart()
		RocheObjProduct = Reports.GetAllProducts()
		DateObj = Reports.GetMinMaxDateFromDatabase()
		return render_to_response('dashboard.html',{'rdata': json.dumps(lis),'mindate':DateObj[0][0],'maxdate': DateObj[0][1], 'products': RocheObjProduct, 'user': request.user},RequestContext(request))
	else:
		HttpResponse("Invalid user")
		logout(request)
		return render_to_response('login.html')


#@app.route("roche/details/",methods=['GET','POST'])
#@login_required(login_url='/')
def ProductDetails(request):
	product = request.GET.get('product_name',None)
	product_names = Reports.GetProductName(product)
	response = HttpResponse(json.dumps(product_names))
	return response

def BatchDetails(request):
	product_name = request.GET.get('product_name',None)
	batch_number = Reports.GetBatchNumber(product_name)
	response = HttpResponse(json.dumps(batch_number))
	return response

def ProductNameChartDetails(request):
	product = request.GET.get('product',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	product_names = Reports.GetChartForProductName(product,from_date,to_date)
	response = HttpResponse(json.dumps(product_names))
	return response

def BatchNumberChartDetails(request):
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	batch_number = Reports.GetChartForBatchNumber(product,product_name,from_date,to_date)
	response = HttpResponse(json.dumps(batch_number))
	return response

def check_for_domain(request):
	email = request.user.email.split("@")[1]
	if email in ['roche.com','solivarlabs.com','solivar.com']:
		return True
	else:
		return False

def BatchNumberChartDetailsFinal(request):
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch_number = request.GET.get('batch_number',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	#print(product,product_name,batch_number,from_date,to_date)
	batch_number = Reports.GetChartForBatchNumberFinal(product,product_name,batch_number,from_date,to_date)
	response = HttpResponse(json.dumps(batch_number))
	return response

def ChartWithDate(request):
	product = request.GET.get('product',None)
	product_name = request.GET.get('product_name',None)
	batch_number = request.GET.get('batch_number',None)
	from_date = request.GET.get('fromDate',None)
	to_date = request.GET.get('toDate',None)
	data = Reports.GetChartFromDateAndTo(product,product_name,batch_number,from_date,to_date)
	response = HttpResponse(json.dumps(data))
	return response

