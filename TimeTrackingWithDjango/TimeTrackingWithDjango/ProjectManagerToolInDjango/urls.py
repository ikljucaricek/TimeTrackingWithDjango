from django.conf.urls import patterns, url
from TimeTrackingWithDjango.ProjectManagerToolInDjango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),)