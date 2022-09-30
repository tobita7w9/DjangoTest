from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Friend
# Create your views here.
"""
class HelloView(TemplateView):
    
    def __init__(self):
        self.params={
            "title":"Hello",
            "form":HelloForm(),
            "result":None
            }
        
    def get(self,request):
        return render(request, "hello/index.html",self.params)

    def post(self, request):
        ch=request.POST.getlist("choice")
        result="<ol><b>selected</b>"
        for item in ch:
            result +="<li>"+item+"</li>"
        result += "</ol>"
        self.params["result"]=result
        self.params["form"]=HelloForm(request.POST)
        return render(request,"hello/index.html" ,self.params)
"""

def index(request):
    data=Friend.objects.all()
    params={
        'title':"Hello",
        'message':'all friends.',
        'data':data,
    }
    return render(request,'hello/index.html',params)
