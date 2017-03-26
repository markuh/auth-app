# coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from authissue.views import AuthView


urlpatterns = [
    # Examples:
    url(r'^$', AuthView.as_view(), name='auth'),
    url(r'^page/$', TemplateView.as_view(template_name="index.html"),
        name='index'),

    url(r'^admin/', include(admin.site.urls)),
]
