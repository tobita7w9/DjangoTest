# -*- coding: utf-8 -*-
from django import forms

class HelloForm(forms.Form):
    check=forms.NullBooleanField(label="Check")