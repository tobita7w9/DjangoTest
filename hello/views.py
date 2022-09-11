from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request,nickname,age):

"""
    if 'msg' in request.GET:
        msg=request.GET["msg"]
        result='you typed: "' + msg + '".'
    else:
        result='please send msg parameter!'
"""    
#    result='your id: '+ str(id)+' , name: "' + nickname + '".'
#    result='your account:' +nickname+'" ('+str(age)+').'
    
#    return HttpResponse(result)

#def index(request):
#    return render(request, "hello/index.html")

def index(request):
    params={
        "title":"Hello/Index",
        "msg":"これはサンプルで作ったページです。",
        "goto":"next"
        }
    return render(request, "hello/index.html",params)

def next(request):
    params={
        "title":"Hello/Next",
        "msg":"これはもうひとつのページです。",
        "goto":"index"
        }
    return render(request,"hello/index.html",params)