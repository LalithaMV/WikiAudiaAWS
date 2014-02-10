from django.conf.urls import patterns, url;
from wa import views;

urlpatterns = patterns('',
	url(r'audio/getimage/(?P<book_id>\d+)/', views.getImage, name = 'getImage'),
	url(r'audio/(?P<book_id>\d+)/', views.audioUpload, name = 'audioUpload'),
	url(r'audio/langBooks/', views.langBooks, name='langBooks'),
    url(r'audio/', views.audioSelection, name='audioSelection'),                                                                                                                   
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
)