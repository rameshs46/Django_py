from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('showDate', views.showDate, name="showDate"),
    path('showDateMsg', views.showDateMsg, name="showDateMsg")
]
