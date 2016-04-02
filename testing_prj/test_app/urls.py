__author__ = 'danleyb2 <ndieksman@gmail.com>'

from test_app import views
from django.conf.urls import url,include

from datetime import datetime

urlpatterns = [
    url(r'^$',views.index),
]