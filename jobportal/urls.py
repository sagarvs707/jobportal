from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    path('register/', include('addcandidates_app.urls')),
    path('adduser/', include('addusers.urls')),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, documemt_root=settings.MEDIA_ROOT)

