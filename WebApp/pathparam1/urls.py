from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('showPathParam1/<str:name>/<int:age>/slug:v>', views.showPathParam1, name="showPathParam1"),
]

