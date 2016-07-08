from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^accounts/profile/$',  views.testView, name='testView'),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),

]
