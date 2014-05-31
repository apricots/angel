from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'angel.views.home', {'template': 'home.html'}, name='home'),
                       url(r'^about/$', 'angel.views.about', {'template': 'about.html'}, name='about'),


                       url(r'^admin/', include(admin.site.urls)),
)
