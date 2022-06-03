from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
import _datetime
from . import models
import json
from django.http import HttpResponse
from django.core import serializers
from myApp.models import Records
import datetime
import pymysql
from config import *
# Create your views here.

from django.http import HttpResponse
def index(request):

    return render(request, "index.html")


def login(request):

    return render(request, "login.html")



# def sort_image(request):
#
#     content = {'sort_flag': False}
#
#     if request.method == 'POST':
#         test_dir = '/home/user/Vincentprp/websystem/static/result'
#         save_dir = '/home/user/Vincentprp/websystem/static/sorted_image'
#         save_mat_dir = '/home/user/Vincentprp/websystem/static/result_feature.mat'
#         return_text = calfunc.sort_all_image(test_dir, save_dir, save_mat_dir)
#         content['sort_flag'] = True
#         content['return_text'] = return_text
#
#     return render(request, "test.html", content)


# def person_detect(request):
#
#     prior = False
#     content = {'fresh': False}
#
#     #web_root = '/home/user/Vincentprp/websystem'
#     web_root = 'D:/prp/ourproject/websystem'
#     video_name = 'c1_2'
#
#     OUTPUT_ROOT = web_root + '/static/result/VID/'
#     INPUT_VIDEO_DIR = web_root + '/static/videos/' + video_name + '.mp4'
#     OUTPUT_PERSON_ROOT = web_root + '/static/result/person/'
#
#     #os.system("python3 /home/user/Vincentprp/websystem/Mask_RCNN/samples/demo2.py --input_video_dir " + INPUT_VIDEO_DIR + " --output_root " + OUTPUT_ROOT + " --output_person_root " + OUTPUT_PERSON_ROOT)
#
#     content['vid_dir'] = OUTPUT_ROOT + video_name + '/' + video_name + '.mp4'
#     #content['vid_dir'] = 'result/VID/' + video_name + '.mp4'
#     # print(content['vid_dir'])
#     test_dir = OUTPUT_PERSON_ROOT + video_name
#     save_dir = web_root + '/static/result/sorted'
#     save_mat_dir = web_root + '/static/result/result_feature.mat'
#     return_text = calfunc.sort_all_image(test_dir, save_dir, save_mat_dir)
#     content['fresh'] = True
#     content['return_text'] = json.dumps(return_text, cls=MyEncoder)
#
#     return render(request, "video.html", content)

def intro(request):

    return render(request, "intro.html")


def monitor(request):

    return render(request, "monitor.html")

def monitor1(request):

    return render(request, "monitor1.html")

def test(request):

    return render(request, "test.html")

def search(request):

    # query_set = records.objects.filter(id=1)  # 查询id=1的数据
    # query_set = records.objects.filter(pswd="123").first()  # 查询第一条数据
    return render(request, "search.html")

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)


def sqlsearch(request):
    query = list(Records.objects.all().values())
    result = {
        "code": 0
        ,"msg": ""
        ,"count": 0,
        "data": []
    }
    result["count"] = len(query)
    result["data"] = list(query)
    print(result["data"])
    # 转换为 JSON 字符串并返回
    return JsonResponse(result)


