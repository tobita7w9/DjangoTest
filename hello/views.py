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
    params={
        'title':"Hello",
        'message':'all friends.',
        'form':HelloForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        num=request.POST['id']
        item=Friend.objects.get(id=num)
        params['data']=[item]
        params['form']=HelloForm(request.POST)
    else:
        params['data']=Friend.objects.all()

    return render(request,'hello/index.html',params)
