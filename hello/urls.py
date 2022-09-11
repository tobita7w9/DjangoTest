# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 22:05:59 2022

@author: flyt-
"""
from django.urls import re_path
from . import views
from .views import HelloView

urlpatterns=[
    re_path('',HelloView.as_view() ,name="index"),
    ]