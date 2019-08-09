from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from .api import portfolioViewSet
from django.urls import path, include, re_path
from . import views

router = routers.DefaultRouter()
router.register('', portfolioViewSet, 'portfolio')

urlpatterns = [
    url('api', include(router.urls)),
    url('', views.home),
]