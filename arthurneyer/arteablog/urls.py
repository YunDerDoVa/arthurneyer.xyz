from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('article/<int:id>', views.article, name="article"),
]
