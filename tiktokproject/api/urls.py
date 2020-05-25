from django.conf.urls import url
from django.urls import include, path
from api.views import *
urlpatterns = [
    path(r'prepare_videourl/', GetVideoUrl.as_view(), name='get-video')
]   
