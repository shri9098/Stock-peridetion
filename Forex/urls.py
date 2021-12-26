"""Forex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from forexapp import views
from forexapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('customer_register/',views.CustomerRegister.as_view({'post':'create'})),
    # path('login_check/',views.Login_check.as_view({'post':'create'})),
    path('logout_check/',views.Logout_check.as_view({'get':'list'})),
    path('newcustomer_register/',views.CustomerRegist.as_view({'post':'create'})),
    path('user_list/',views.CustomerRegist.as_view({'get':'list'})),
    path('login/',views.Login.as_view({'post':'create'})),

    path('forexapi/',views.ForexApi.as_view({'get':'list'})),
    path('Indicatores/',views.Indicatores.as_view({'get':'list'})),
    path('orderdetailsApi/',views.OrderdetailsApi.as_view({'post':'create'})),



]
