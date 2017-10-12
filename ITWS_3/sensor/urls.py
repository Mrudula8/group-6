from django.conf.urls import url
from . import views
app_name='sensor'

urlpatterns = [
    url(r'^$', views.result, name='index'),
    url(r'^detail',views.detail, name='detail'),
]
