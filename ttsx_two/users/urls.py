from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^check_username/$', views.check_username, name='check_username'),
    url(r'^check_usermail/$', views.check_usermail, name='check_usermail'),

    url(r'^login/$', views.login, name='login'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^centerinfo/$', views.centerinfo, name='centerinfo'),
    url(r'^recv_message_handle/$', views.recv_message_handle, name='recv_message_handle'),

    url(r'^centerorder/$', views.centerorder, name='centerorder'),
    url(r'^centersite/$', views.centersite, name='centersite'),

]



