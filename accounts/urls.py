from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import login_page, RegisterView, Home_view

urlpatterns = [
    url(r'signup/$', RegisterView, name='register'),
    url(r'login/$', login_page, name='login'),
    # url(r'logout/$', logout_view, name='logout'),
    url(r'home/$', Home_view, name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documemt_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, documemt_root=settings.MEDIA_ROOT)