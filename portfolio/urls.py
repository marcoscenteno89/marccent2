from django.conf.urls import url
from rest_framework import routers
from .api import portfolioViewSet
from django.urls import path, include, re_path
from . import views

router = routers.DefaultRouter()
router.register('api', portfolioViewSet, 'portfolio')

urlpatterns = [
    url('api', include(router.urls))
]

urlpatterns += [
    url('', views.home)
    # re_path(r'(?P<path>.*)', views.home)
]