from django.conf.urls import url
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from api.views import GetVideoUrl
from django.views.decorators.csrf import csrf_exempt #убрать

urlpatterns = [
    path('', views.index, name='index'),
]