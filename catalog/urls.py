"""mycoins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('coins/', views.CoinListView.as_view(), name='coins'),
    path('coins/<int:pk>', views.CoinDetailView.as_view(), name='coin-detail'),
    path('rulers/', views.RulersListView.as_view(), name='rulers'),
    path('rulers/<int:pk>', views.RulersDetailView.as_view(), name='ruler-detail'),
]
