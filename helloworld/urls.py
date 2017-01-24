from django.conf.urls import url
from . import views

urlpatterns = [
    #homepage of app helloworld
    url(r'^$', views.index, name='index'),
    
    #/helloworld/id of bsit table
    url(r'^(?P<BSIT_id>[0-9]+)$', views.details, name='details'),
    
]