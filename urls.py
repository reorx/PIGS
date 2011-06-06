from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

#views#
#from django.contrib.auth.views import login, logout
from default.views import home

urlpatterns = patterns('',
    (r'^$',home),
    (r'^knowledge/', include('default.knowledge.urls')),
    (r'^blog/', include('blog.urls')),
    #admin#
    (r'^admin/',include(admin.site.urls)),
    #static#
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
