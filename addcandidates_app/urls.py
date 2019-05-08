from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import job_view, validate_registration_otp, resend_otp, view_all_candidate, \
    view_all_candidate_count, valid_candidate_count, AddCondidate, not_valid

urlpatterns = [
    url(r'it_jobs/$', job_view, name='it_jobs'),

    url(r'verify_otp/$', validate_registration_otp, name='verify_otp'),
    url(r'resend_otp/$', resend_otp, name='verify_otp'),

    url(r'^get/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),
    url(r'^delete/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),
    url(r'^put/(?P<id>[0-9A-Fa-f-]+)/$', AddCondidate.as_view()),

    url(r'view_all/$', csrf_exempt(view_all_candidate), name='view_all'),
    url(r'view_all_count/$', csrf_exempt(view_all_candidate_count), name='view_all'),
    url(r'valid_count/$', csrf_exempt(valid_candidate_count), name='valid_count'),

    path('not_valid/', not_valid, name='not_valid')
]
