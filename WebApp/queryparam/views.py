from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def showGetParam(request):
    name = request.GET.get('name')
    return HttpResponse('Passed name is %s' %name)

def showMoreParam(request):
    name = request.GET.get('name')
    age = int(request.GET.get('age'))
    return HttpResponse('Name = %s Age = %d' % (name,age))

def showDefault(request):
    name = request.GET.get('name','Not Found')
    return HttpResponse('Name = %s' % name)

