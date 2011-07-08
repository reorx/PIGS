import os
from django.conf.urls.defaults import *

urlpatterns = patterns('django.contrib.auth.views',
    (r'^account/login/', 'login', {'template_name':'me/login.html'}),
    (r'^account/logout/', 'logout'),
)
urlpatterns += patterns('me.views',
    (r'^$', 'Entrance'),
    (r'^ajax/category_create_form/$', 'c_c_f'),
)
urlpatterns += patterns('knowledge.views',
    (r'^know/$', 'ReadKnow'),
    (r'^know/db/$', 'WriteKnow'), # create, update, delete
    (r'^know/category/$', 'ReadKnowCategory'),
    (r'^know/category/db/$', 'WriteKnowCategory'), # create, update, delete
    (r'^know/segment/$', 'ReadKnowSegment'),
    (r'^know/segment/db/$', 'WriteKnowSegment'), # create, update, delete
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
