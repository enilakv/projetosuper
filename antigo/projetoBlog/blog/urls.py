from django.conf.urls import include, url
from . import views

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post_list/$', views.post_list),
]
