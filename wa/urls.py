from django.conf.urls import patterns, url;
from wa import views;

urlpatterns = patterns('',
    url(r'^$', views.audio, name='audio'),
)