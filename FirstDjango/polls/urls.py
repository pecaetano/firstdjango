'''
Created on Oct 9, 2016

@author: Paulo
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]