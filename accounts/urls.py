from django.conf.urls import url
from .views import login_page, RegisterView

urlpatterns = [
    url(r'signup/$', RegisterView, name='register'),
    url(r'login/$', login_page, name='login'),
]
