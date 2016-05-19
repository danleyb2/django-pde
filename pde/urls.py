from pde import views
from django.conf.urls import url,include

from datetime import datetime

urlpatterns = [
    url(r'^$',views.index),
]