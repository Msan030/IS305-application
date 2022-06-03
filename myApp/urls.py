from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url,include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login$', views.login),
    url(r'^index$', views.index),
    url(r'^intro$', views.intro),
    url(r'^monitor$', views.monitor),
    url(r'^monitor1$', views.monitor1),
    url(r'^test$', views.test),
    url(r'^search$', views.search),
    path('sqlsearch', views.sqlsearch),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': 'D:/prp/ourproject/websystem/static'}),


    # url(r'^evaluate$', view.evaluate),
    # url(r'^test$', view.sort_image),
    # url(r'^video$', view.person_detect),
]