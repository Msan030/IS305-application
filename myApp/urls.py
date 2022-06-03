from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
from django.urls import path
from . import views
from . import login
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
    url(r'^personal', views.personal),
    url(r'^signup$', views.signup),
    url(r'^login2$', views.login2),
    url(r'^signup2$', views.signup2),
    url(r'^searchtest$', views.searchtest),
    path('sqlall', views.sqlall),
    path('sqlsearch', views.sqlsearch),
    path('sqlpersonal', views.sqlpersonal),
    path('sqlbd1', views.sqlbd1),
    path('sqlhandle', views.sqlhandle),
    path('sqllogin', views.login),

]