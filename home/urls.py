from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = 'Text Utils'

urlpatterns = [
    path('', views.index, name='index'),
     path('analyze', views.analyze, name='analyze')
]
