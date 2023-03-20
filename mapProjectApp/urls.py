from django.urls import path
from mapProjectApp import views
from .views import get_json_data, get_json_notice

print('mapProjectApp.urls.py will load')

urlpatterns = [
    path('', views.index, name='homepage'),
    path('qrcode/', views.qrcode, name='qrcode'),
    path('main/', views.main, name='main'),
    path('main/map/', views.map, name='map'),

    path('main/mission/', views.mission, name='mission'),

    path('main/notice/', views.notice, name='notice'),

    path('main/userinfo/', views.userinfo, name='userinfo'),
    path('get_json_data/', get_json_data),
    path('get_json_notice', get_json_notice)
    # path('main/<str:name>', views.rederict, name='rederict')
]
print('mapProjectApp.urls.py is loaded')
