from django.urls import path
from mapProjectApp import views
print('mapProjectApp.urls.py will load')

urlpatterns = [
    path('', views.index, name='homepage'),
    path('qrcode/', views.qrcode, name='qrcode'),
    path('main/', views.main, name='main'),
    path('map/', views.map, name='map'),
    path('mission/', views.mission, name='mission'),
    path('notice/', views.notice, name='notice'),
    path('userinfo/', views.userinfo, name='userinfo'),

]
print('mapProjectApp.urls.py is loaded')