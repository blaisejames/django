from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'register/$', views.reg),
    url(r'login/$', views.login),
    url(r'users/new/$', views.reg),
    url(r'users/$', views.index),
]