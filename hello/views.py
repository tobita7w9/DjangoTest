from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Friend
from django.db.models import QuerySet
# Create your views here.
def __new_str__(self):
    result=''
    for item in self:
        result='<tr>'
        for k in item:
            result+='<td>'+str(k)+'='+str(item[k])+'</td>'
        result+='</tr>'
    return result

QuerySet.__str__=__new_str__


def index(request):
    data=Friend.objects.all().values('id','name','age')
    params={
        'title':'Hello',
        'data':data,
    }
    return render(request,'hello/index.html',params)
