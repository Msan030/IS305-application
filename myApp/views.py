from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import RequestContext
import datetime
import json
import _datetime

import project.settings
from yolo import predict_yolo
from . import models
from myApp.models import Records
from django.db.models import Q
from myApp.models import Users
import hashlib
from project.settings import *
from . import  database
# Create your views here.

from django.http import HttpResponse

def computeMD5(message):
    # 创建md5对象
    m = hashlib.md5()
    # Tips
    # 此处必须声明encode
    # 若写法为m.update(str) 报错为： Unicode-objects must be encoded before hashing
    if message != "":
        m.update(message.encode(encoding='utf-8'))
        return m.hexdigest()
    else:
        return ""

def index(request):

    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwd = computeMD5(password)
        if Users.objects.filter(Q(username=username)&Q(passwd=passwd)):
            return JsonResponse({"status": 1})
        else:
            return JsonResponse({"status": 0})
    else:
        return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwd = computeMD5(password)
        if Users.objects.filter(username=username):
            return JsonResponse({"status":0})
        else:
            Users.objects.create(username=username, passwd=passwd,id=1)
            return JsonResponse({"status":1})
    else :
        return render(request, "signup.html")

def intro(request):

    return render(request, "intro.html")

def img(request):
    if request.method == 'POST':
        file = request.FILES.get('file')  # 获取前端上传的文件
        print(type(file))
        fix = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '1'  # 给文件加前缀防止文件名重复
        # 以下用绝对路径存储文件，之前我用相对路径一直写不对
        curPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

        # InfoServiceSystem是项目名
        # rootPath = curPath[:curPath.find("Tra\\") + len("itemplus\\")]
        img_path = os.path.abspath(curPath + '/static/upimg.jpg' )
        print(img_path)
        # 返回给前端的图片路径用相对路径，前端用绝对路径反而加载不了图片
        img_path_res = '/static/upimg.jpg'
        f = open(img_path, 'wb')
        for i in file.chunks():
            f.write(i)
        f.close()
        img_path_o = os.path.abspath(curPath + '/static/upimg-'+ fix+ '.jpg')
        f = open(img_path_o, 'wb')
        for i in file.chunks():
            f.write(i)
        f.close()
        img_path_abo = os.path.abspath(curPath + '/static/outimg.jpg')
        imgOutput = predict_yolo.YoloDetect.imageDetect(img_path,img_path_abo)
        # imgOutput=[{"rcat" : "纸箱"}]
        for i in range (len(imgOutput)):
            add={
                "rcat" : imgOutput[i]["rcat"],
                "rphoto" : '/static/upimg-'+ fix+ '.jpg'
            }
            database.sqladd(add)
        return JsonResponse({'img_name': img_path_res})

def video(request):
    if request.method == 'POST':
        file = request.FILES.get('file')  # 获取前端上传的文件
        print(type(file))
        # fix = datetime.date.today().strftime('%Y%m%d') + '1'  # 给文件加前缀防止文件名重复
        # 以下用绝对路径存储文件，之前我用相对路径一直写不对
        curPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

        # InfoServiceSystem是项目名
        # rootPath = curPath[:curPath.find("Tra\\") + len("itemplus\\")]
        vi_path = os.path.abspath(curPath + '/static/upvideo.mp4')
        print(vi_path)
        # 返回给前端的图片路径用相对路径，前端用绝对路径反而加载不了图片
        vi_path_res = '/static/upvideo.mp4'
        f = open(vi_path, 'wb')
        for i in file.chunks():
            f.write(i)
        f.close()

        # imgOutput = predict_yolo.YoloDetect.imageDetect(img_path)
        # database.sqladd(imgOutput)
        return JsonResponse({"status":1})
    else :
        return JsonResponse({"status":0})

def monitor(request):

    return render(request, "monitor.html")

def monitor1(request):

    return render(request, "monitor1.html")

def monitor2(request):
    # fix = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '1'  # 给文件加前缀防止文件名重复
    # # 以下用绝对路径存储文件，之前我用相对路径一直写不对
    # curPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #
    # # InfoServiceSystem是项目名
    # # rootPath = curPath[:curPath.find("Tra\\") + len("itemplus\\")]
    # vi_path = os.path.abspath(curPath + '/static/upvideo.mp4')
    #
    # vi_path_abo = os.path.abspath(curPath + '/static/outvideo.mp4')
    # predict_yolo.YoloDetect.videoDetect(vi_path,vi_path_abo)
    return render(request, "monitor2.html")

def test(request):

    return render(request, "test.html")

def search(request):

    return render(request, "search.html")

def personal(request):

    return render(request, "personal.html")

def login2(request):

    return render(request, "login2.html")

def signup2(request):

    return render(request, "signup2.html")

def searchtest(request):

    return render(request, "searchtest.html")



###显示未处理###
def sqlall(request):
    query = list(Records.objects.filter(isHandle=0).values())
    result = {
        "code": 0
        ,"msg": ""
        ,"count": 0,
        "data": []
    }
    result["count"] = len(query)
    result["data"] = list(query)
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)

###搜索框###
def sqlsearch(request):
    rid=request.POST.get("id")
    rfloor=request.POST.get("rfloor")
    rbuilding=request.POST.get("rbuilding")
    rcat=request.POST.get("rcat")
    date1=request.POST.get("date1")
    date2=request.POST.get("date2")
    flag=[0,0,0,0]
    c=["纸箱","自行车","家具","鞋架","其他"]
    if date1=="":
        date1="1970-1-1"
    if date2=="":
        date2="2023-12-31"
    rdate1=datetime.datetime.strptime(date1,"%Y-%m-%d")
    rdate2=datetime.datetime.strptime(date2,"%Y-%m-%d")
    qu = Records.objects.filter(Q(isHandle=0)&Q(rdate__gt=rdate1)&Q(rdate__lt=rdate2))
    if rid!="":
        flag[0]=1
        qu = qu.filter(id=int(rid))
    if rfloor!="":
        flag[1]=1
        qu = qu.filter(rfloor=int(rfloor))
    if rbuilding!="":
        flag[2]=1
        qu = qu.filter(rbuilding=int(rbuilding))
    if rcat!="":
        flag[3] = 1
        qu = qu.filter(rcat=c[int(rcat)])
    query=list(qu.values())

    result = {
        "code": 0
        ,"msg": ""
        ,"count": 0,
        "data": []
    }
    result["count"] = len(query)
    result["data"] = list(query)
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)

###个人中心 显示已处理###
def sqlpersonal(request):
    query = list(Records.objects.filter(isHandle=1).values())
    result = {
        "code": 0
        ,"msg": ""
        ,"count": 0,
        "data": []
    }
    result["count"] = len(query)
    result["data"] = list(query)
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)

###全局监控 显示居民楼1###
def sqlbd1(request):
    query = list(Records.objects.filter(rbuilding=1).values())
    result = {
        "code": 0
        ,"msg": ""
        ,"count": 0,
        "data": []
    }
    result["count"] = len(query)
    result["data"] = list(query)
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)

###点击已处理###
def sqlhandle(request):
    strdata = request.POST.get("id")
    print(strdata)
    if strdata!="[]":
        listdata=strdata[1:-1].split(",{")
        for i in range(len(listdata)):
            if i>0:
                listdata[i]="{"+listdata[i]
            jdata=json.loads(listdata[i])
            Records.objects.filter(id=int(jdata['id'])).update(isHandle=1)
    query = list(Records.objects.filter(isHandle=0).values())
    result = {
        "code": 0
        ,"msg": ""
        ,"count": 0,
        "data": []
    }
    result["count"] = len(query)
    result["data"] = list(query)
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)