from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def showPathParam1(request,name,age,v):
    return HttpResponse('Path Param is %s and age is %d, slug is %s '% (name, age, v))
