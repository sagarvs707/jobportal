from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from .views import addcondidate_view, validate_registration_otp, resend_otp, view_all_candidate, \
    view_all_candidate_count, valid_candidate_count, AddCondidate, not_valid

urlpatterns = [
    url(r'addcondidate/$', csrf_exempt(addcondidate_view), name='addcondidate'),
    url(r'verify_otp/$', csrf_exempt(validate_registration_otp), name='verify_otp'),
    url(r'resend_otp/$', csrf_exempt(resend_otp), name='verify_otp'),

    url(r'^get/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),
    url(r'^delete/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),
    url(r'^put/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),

    url(r'view_all/$', csrf_exempt(view_all_candidate), name='view_all'),
    url(r'view_all_count/$', csrf_exempt(view_all_candidate_count), name='view_all'),
    url(r'valid_count/$', csrf_exempt(valid_candidate_count), name='valid_count'),

    path('not_valid/', not_valid, name='not_valid')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documemt_root=settings.MEDIA_ROOT)
