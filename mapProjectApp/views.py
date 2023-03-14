from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
import configparser
import qrcode as qr
import datetime
import json

from mapProjectApp import models

print('mapProjectApp.views.py will load')


def get_id():
    config = configparser.ConfigParser()
    config.read(r'mapProjectApp/carid.ini')
    id_value = config.get('global', 'id')
    return id_value


userinfomation = {
    'id': '',
    'gender': '',
    'name': '',
    'phone': '',
    'age': '',
    'work_id': '',
    'position': '',
    'carid': get_id(),
}  # 得到用户id后进入数据库查询用户信息并保存在这个字典中


def index(request):
    return render(request, 'mapProject/index.html')


def qrcode(request):
    data = {
        'id': get_id(),
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    qrimg = qr.QRCode(border=0)
    qrimg.add_data(json.dumps(data))
    qrimg.make(fit=True)
    qrimg = qrimg.make_image(fill_color=(255, 255, 255), back_color=(35, 61, 91))
    qrimg.save('mapProjectApp/static/images/qrcode/test1.png')
    return render(request, 'mapProject/qrcode.html', {'qrimg': qrimg})


# 扫码后等待服务器返回身份数据，接收到之后从数据库中匹配信息并保存在userinfomation中

def check(request,id):
    pass

def main(request):
    return render(request, 'mapProject/main.html', userinfomation)


def map(request):
    return render(request, 'mapProject/map.html', userinfomation)


def mission(request):
    return render(request, 'mapProject/mission.html', userinfomation)


def notice(request):
    return render(request, 'mapProject/notice.html', userinfomation)


def userinfo(request):
    return render(request, 'mapProject/userinfo.html')


def rederict(request, name):
    return render(request, 'mapProject/' + name + '.html', userinfomation)


print('mapProjectApp.views.py is loaded')
