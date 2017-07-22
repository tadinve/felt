"""GoogleSignin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from roche_app import views


urlpatterns = [
    url(r'^home/$', views.home,name="home"),
    url(r'^dashboard/$', views.dashboard,name="dashboard"),
    url(r'^ProductDetails/$', views.ProductDetails,name="ProductDetails"),
    url(r'^BatchDetails/$', views.BatchDetails,name="BatchDetails"),
    url(r'^ProductNameChartDetails/$', views.ProductNameChartDetails,name="ProductNameChartDetails"),
    url(r'^BatchNumberChartDetailsFinal/$', views.BatchNumberChartDetailsFinal,name="BatchNumberChartDetailsFinal"),
    url(r'^BatchNumberChartDetails/$', views.BatchNumberChartDetails,name="BatchNumberChartDetails"),
    url(r'^BrrPriorityReport/$', views.BrrPriorityReport,name="BrrPriorityReport"),
    url(r'^logout/$',views.logout,name="logout"),
]