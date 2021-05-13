from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="greentea_home"),
    path('artyp/', views.home, name="artyp"),
]
