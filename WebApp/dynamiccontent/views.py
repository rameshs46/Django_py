from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import date

def showDate(request):
    return HttpResponse("<h1>%s</h1>" % date.today())

def showDateMsg(request):
    return HttpResponse("<h1>%s</h1>" % date.strftime(date.today(), 'Current date is %d %b %Y'))
