from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import RequestContext
import datetime
import json
import _datetime
from . import models
from myApp.models import Records
import datetime

# data={
#     "rdate": xxxx-xx-xx,
#     "rbuilding": num,
#     "rfloor": num,
#     "rcat": (该参数为以下值之一：纸箱、自行车、家具、鞋架、其他),
#     "rphoto": path
# }

#######   example    ######
# data = {
#     "rcat": "纸箱",
#     "rphoto": "../static/people/video1-3.png"
# }
# database.sqladd(data)

def sqladd(data):
    rid=len(list(Records.objects.all().values()))+1
    rdate=datetime.date.today()
    rcat=data["rcat"]
    rphoto=data["rphoto"]
    flag = Records.objects.create(
        id=rid,
        rdate=rdate,
        rbuilding=1,
        rfloor=1,
        rcat=rcat,
        rphoto=rphoto,
        isHandle=0,
        isDelete=0
        )
    if flag:
        return JsonResponse({"status":"add success!"})
    return JsonResponse({"status":"failed!"})