from django.conf.urls import patterns, url

from treatment import views

urlpatterns = patterns('',
    # ex: /treatment/
    url(r'^$', views.index, name='index'),
    # ex: /treatment/1/
    url(r'^(?P<treatment_id>\d+)/$', views.detail, name='detail')
)
