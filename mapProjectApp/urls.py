from django.urls import path
from mapProjectApp import views

urlpatterns = [
    path('', views.index, name='homepage'),
]
