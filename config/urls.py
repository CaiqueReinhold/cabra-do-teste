from django.conf import settings
from django.conf.urls import url, include, static


urlpatterns = [
    url(r'^', include('tests_app.urls', namespace='tests')),
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL,
                                 document_root=settings.MEDIA_ROOT)
