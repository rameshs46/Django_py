from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('showGetParam', views.showGetParam, name="showGetParam"),
    path('showMoreParam', views.showMoreParam, name="showMoreParam"),
    path('showDefault', views.showDefault, name="showDefault")
]