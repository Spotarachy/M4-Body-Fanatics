from django.contrib import admin
from django.urls import path
from . import views
from django.db import models

urlpatterns = [
    path('', views.index, name='home'),  
] 