from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('article/<str:slug>', views.article, name="article"),
]
