from django.conf.urls import url
from django.urls import path
from .views import AddUser

from .views import register_user, login_user, change_password, get_all_users

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('login_user/', login_user, name='login_user'),
    path('change_pass/', change_password, name='change_pass'),
    path('get_all_users/', get_all_users, name='get_all_users'),

    url(r'^get/(?P<id>[0-9A-Fa-f-]+)/$', AddUser.as_view()),
    url(r'^delete/(?P<id>[0-9A-Fa-f-]+)/$', AddUser.as_view()),
    url(r'^put/(?P<id>[0-9A-Fa-f-]+)/$', AddUser.as_view()),

]