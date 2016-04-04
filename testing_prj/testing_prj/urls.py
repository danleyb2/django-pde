
from django.conf.urls import url,include
from django.contrib import admin
#from test_app import views
#from pa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pa_dev/',include('package_dev.urls')),
    #url(r'^pa/',include('pa.urls')),
]
