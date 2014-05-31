from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'angel.views.home', {'template': 'home.html'}, name='home'),
                       url(r'^about/$', 'angel.views.about', {'template': 'about.html'}, name='about'),
                       url(r'^register/$', 'users.views.register', {'template': 'register.html'}, name='register'),
                       url(r'^login/$', 'users.views.user_login', {'template': 'login.html'}, name='login'),
                       url(r'^logout/$', 'users.views.user_logout', name='logout'),
                       url(r'^admin/', include(admin.site.urls)),
)
