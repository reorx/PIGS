from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$',home),
    (r'^knowledge/', include('default.knowledge.urls')),
    (r'^blog/', include('blog.urls')),
)

# enable admin
from config import ADMIN
if ADMIN:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += patterns(
        (r'^admin/',include(admin.site.urls)),
    )

# enable static server in debug mode
from settings import DEBUG, MEDIA_ROOT
if DEBUG:
    import os.path
    ROOT = os.path.dirname(__file__)
    STATIC_ROOT = os.path.join(ROOT, '../static')
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': STATIC_ROOT
        }),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT
        }),
    )
