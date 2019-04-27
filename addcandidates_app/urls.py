from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from .views import addcondidate_view, validate_registration_otp, AddCondidate

urlpatterns = [
    url(r'addcondidate/$', csrf_exempt(addcondidate_view), name='addcondidate'),
    url(r'verify_otp/$', csrf_exempt(validate_registration_otp), name='verify_otp'),

    url(r'^get/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),
    url(r'^delete/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),
    url(r'^put/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documemt_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, documemt_root=settings.MEDIA_ROOT)