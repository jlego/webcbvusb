from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^$', 'webcbvusb.views.frontpage', name='frontpage'),
    url(r'^estadisticas/$', 'webcbvusb.views.stats', name='stats'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)
