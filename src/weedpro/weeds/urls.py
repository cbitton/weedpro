from django.conf.urls import patterns, url

from weeds import views

urlpatterns = patterns('',
    # ex: /weeds/
    url(r'^$', views.index, name='index'),
    # ex: /weeds/1/
    url(r'^(?P<weed_id>\d+)/$', views.detail, name='detail')
)
