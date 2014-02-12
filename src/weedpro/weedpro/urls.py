from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'weedpro.views.home', name='home'),
    url(r'^detail/', 'weedpro.views.detail', name='detail'),
    url(r'^treatment/', include('treatment.urls', namespace="treatment")),
    url(r'^weeds/', include('weeds.urls', namespace="weeds")),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
