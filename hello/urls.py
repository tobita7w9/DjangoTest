# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 22:05:59 2022

@author: flyt-
"""

from django.urls import path
from . import views

urlpatterns=[
    #path('my_name_is_<nickname>.I_am_<int:age>_years_old.',views.index,name="index"),
    path('',views.index,name="index"),
    path('next',views.next,name='next'),
    ]