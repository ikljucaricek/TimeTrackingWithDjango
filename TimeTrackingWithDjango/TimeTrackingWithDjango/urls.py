from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'TimeTrackingWithDjango.ProjectManagerToolInDjango.views.index', name = 'home'),
    #url(r'^$', 'TimeTrackingWithDjango.views.home', name='home'),
    #url(r'^TimeTrackingWithDjango/', include('TimeTrackingWithDjango.TimeTrackingWithDjango.urls')),
    #url(r'^ProjectManagerToolInDjango/', include(ProjectManagerToolInDjango.urls)),
    url(r'^$', 'TimeTrackingWithDjango.ProjectManagerToolInDjango.views.osobaprojekt', name='index'),
    url(r'^osobaprojekt/', 'TimeTrackingWithDjango.ProjectManagerToolInDjango.views.osobaprojekt'),
    url(r'^osoba/$', 'TimeTrackingWithDjango.ProjectManagerToolInDjango.views.osobe'),
    url(r'^projekt/', 'TimeTrackingWithDjango.ProjectManagerToolInDjango.views.projekti'),
    #url(r'^osoba/?q=$', 'TimeTrackingWithDjango.ProjectManagerToolInDjango.views.search'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
