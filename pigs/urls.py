import os
from django.conf.urls.defaults import *

urlpatterns = patterns('django.contrib.auth.views',
    (r'^account/login/', 'login', {'template_name':'me/login.html'}),
    (r'^account/logout/', 'logout'),
    #(r'^account/settings/', 'settings'),
)
urlpatterns += patterns('',
    (r'^$', 'me.views.site_entrance'),
    (r'^know/', include('me.urls')),
)
#urlpatterns += patterns('.views',
    #(r'^/', ''),
#)


from settings import ADMIN, DEBUG, MEDIA_ROOT
# enable admin
if ADMIN:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += patterns('',
        (r'^admin/',include(admin.site.urls)),
    )
# enable static server in debug mode
if DEBUG:
    ROOT = os.path.dirname(__file__)
    STATIC_ROOT = os.path.join(ROOT, '../static')
    urlpatterns += patterns( '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': STATIC_ROOT
        }),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT
        }),
    )
