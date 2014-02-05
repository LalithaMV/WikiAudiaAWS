from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikiaudia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^wikiaudia/', include('wa.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
