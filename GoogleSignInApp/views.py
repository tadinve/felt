from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from GoogleSignInApp import Reports
# from django.template.context import RequestContext
from django.http import HttpResponse
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
		return render_to_response('home.html', {'rdata': json.dumps(lis)})
	else:
		HttpResponse("Invalid user")
		logout(request)
		return render_to_response('login.html')


def logout(request):
	auth_logout(request)
	return redirect('/')

def check_for_domain(request):
	email = request.user.email.split("@")[1]
	if email in ['roche.com','solivarlabs.com','solivar.com']:
		return True
	else:
		return False
