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
import time
from mapProjectApp import models
from django.http import JsonResponse
from .utils import read_json_file

print('mapProjectApp.views.py will load')

start_time = 0
counter = 0


def get_id():
    config = configparser.ConfigParser()
    config.read(r'mapProjectApp/carid.ini')
    id_value = config.get('global', 'id')
    return id_value


userinformation = {
    'id': 1,
    'gender': 'test_gender',
    'name': 'test_name',
    'phone': 'test_phone_number',
    'age': 'test_age',
    'work_id': 'test_work_id',
    'position': 'test_position',
    'carid': get_id(),
}  # 得到用户id后进入数据库查询用户信息并保存在这个字典中


def index(request):
    return render(request, 'mapProject/index.html')


def qrcode(request):
    for i in userinformation.keys():
        userinformation[i] = ''
    userinformation['carid'] = get_id()
    data = {
        'id': get_id(),
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    qrimg = qr.QRCode(border=0)
    qrimg.add_data(json.dumps(data))
    qrimg.make(fit=True)
    qrimg = qrimg.make_image(fill_color=(255, 255, 255), back_color=(35, 61, 91))
    qrimg.save('mapProjectApp/static/images/qrcode/qrcode.png')
    return render(request, 'mapProject/qrcode.html')


# 扫码后等待服务器返回身份数据，接收到之后从数据库中匹配信息并保存在userinfomation中

def check(request, id: json):
    user = models.Employee.objects.filter(id=id.id)
    if len(user) == 1:
        user = user[0]
        userinformation['id'] = user.id
        userinformation['gender'] = user.gender
        userinformation['name'] = user.name
        userinformation['phone'] = user.phone
        userinformation['age'] = user.age
        userinformation['work_id'] = user.work_id
        userinformation['position'] = user.position
        return render(request, 'mapProject/main.html')
    else:  # 如果没有找到用户，返回错误页面
        # return render(request,'mapProject/error.html')
        pass


def main(request):
    global start_time, counter
    counter += 1
    if counter == 1:
        start_time = time.time()
    print('main is loaded   ', start_time)
    return render(request, 'mapProject/main.html', userinformation)


def get_json_data(request):
    file_path = 'mapProjectApp/static/json/data.json'
    data = read_json_file(file_path)
    return JsonResponse(data)


def get_json_notice(request):
    file_path = "mapProjectApp/static/json/notice.json"
    data = read_json_file(file_path)
    return JsonResponse(data)


def map(request):
    return render(request, 'mapProject/map.html', userinformation)


def mission(request):
    # 查找数据库中mission表中所有carrier_id为当前用户id的任务
    missions = models.Mission.objects.filter(carrier_id=userinformation['id'])
    # 将任务分为已完成、未完成、已取消、进行中四类
    finished_missions = []
    unfinished_missions = []
    canceled_missions = []
    ongoing_missions = []
    loc = models.Location.objects.all()
    # 将loc转化为城市名和经纬度元组的json
    loc_json = []
    for i in loc:
        loc_json.append([i.name, i.longitude, i.latitude])

    print(missions)
    try:
        for mission in missions:
            if mission.status == '已完成':
                finished_missions.append(mission)
            elif mission.status == '未完成':
                unfinished_missions.append(mission)
            elif mission.status == '已取消':
                canceled_missions.append(mission)
            else:
                ongoing_missions.append(mission)
        # 将任务按照departure_time排序
        finished_missions.sort(key=lambda x: x.departure_time)
        unfinished_missions.sort(key=lambda x: x.departure_time)
        canceled_missions.sort(key=lambda x: x.departure_time)
        ongoing_missions.sort(key=lambda x: x.departure_time)
    except:
        pass

    return render(request, 'mapProject/mission.html',
                  {'userinformation': userinformation, 'finished_missions': finished_missions,
                   'unfinished_missions': unfinished_missions, 'canceled_missions': canceled_missions,
                   'ongoing_missions': ongoing_missions, 'loc': loc_json})


def notice(request):
    return render(request, 'mapProject/notice.html', userinformation)


def time_format():
    global start_time
    time_num = time.time() - start_time
    print("start_time:", start_time)
    print('time:', time_num)
    if time_num < 60:
        return str(int(time_num)) + '秒'
    elif time_num < 3600:
        return str(int(time_num / 60)) + '分' + str(int(time_num % 60)) + '秒'
    else:
        return str(int(time_num / 3600)) + '时' + str(int(time_num % 3600 / 60)) + '分' + str(int(time_num % 60)) + '秒'


def userinfo(request):
    # 查找数据库中mission表中所有carrier_id为当前用户id的任务
    missions = models.Mission.objects.filter(carrier_id=userinformation['id'])
    # 将任务分为已完成、未完成、已取消、进行中四类
    finished_missions = []
    unfinished_missions = []
    canceled_missions = []
    ongoing_missions = []
    try:
        for mission in missions:
            if mission.status == '已完成':
                finished_missions.append(mission)
            elif mission.status == '未完成':
                unfinished_missions.append(mission)
            elif mission.status == '已取消':
                canceled_missions.append(mission)
            else:
                ongoing_missions.append(mission)
        # 将任务按照departure_time排序
        finished_missions.sort(key=lambda x: x.departure_time)
        unfinished_missions.sort(key=lambda x: x.departure_time)
        canceled_missions.sort(key=lambda x: x.departure_time)
        ongoing_missions.sort(key=lambda x: x.departure_time)
    except:
        pass
    print(userinformation)
    return render(request, 'mapProject/userinfo.html',
                  {'user': userinformation, 'using_time': time_format(), 'userinformation': userinformation,
                   'finished_missions': finished_missions,
                   'unfinished_missions': unfinished_missions})


def rederict(request, name):
    if name == 'userinfo':
        userinfo(request)
    elif name == 'mission':
        mission(request)
    elif name == 'notice':
        notice(request)
    elif name == 'map':
        map(request)
    else:
        pass
    # return render(request, 'mapProject/' + name + '.html', userinformation)


print('mapProjectApp.views.py is loaded')
