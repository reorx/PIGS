from django.conf.urls.defaults import *

urlpatterns = patterns('me.views',
    (r'^$', 'know_home'),
    (r'^r/(?P<nid>\w+)/$', 'know_read'),
    (r'^w/$', 'know_write_create'),
    (r'^w/(?P<nid>\w+)/$', 'know_write_modify'),

    (r'^category/$', 'cate_home'),
    (r'^category/r/(?P<nid>\w+)/$', 'cate_read'),
    (r'^category/w/$', 'cate_write_create'),
    (r'^category/w/(?P<nid>\w+)/$', 'cate_write_modify'),
    #(r'^segment/$', 'ReadKnowSegment'),
    #(r'^segment/db/$', 'WriteKnowSegment'), # create, update, delete
)
