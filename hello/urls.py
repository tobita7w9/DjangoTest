# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 22:05:59 2022

@author: flyt-
"""
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index ,name="index"),
    ]