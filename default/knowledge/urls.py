from django.conf.urls.defaults import *
from my_PIGS.default.knowledge.views import *

urlpatterns = patterns('',
    (r'^$', index),
    #page request
    (r'^view_k_list/', view_k_list),
    (r'^view_category/', infoarea_category),
    (r'^content_knowledge/', content_knowledge),
    (r'^extend_k_info/', extend_k_info),
    #editor
    (r'^editor_contentpart/', editor_contentpart),
    (r'^editor_extendpart/', editor_extendpart),
    #sql: knowledge
    (r'^create/', create_or_change),
    (r'^change/', create_or_change),
    (r'^delete/', delete),
    #sql: content
    (r'^add_content/', add_content),
    #ajax
    (r'^ajax_certify/', ajax_certify),
    (r'^ajax_parent/', ajax_parent),
    #tip
    (r'^add_tip/', add_tip),
    (r'^change_tip/', change_tip),
    # get
    (r'^get_parent_title/', get_parent_title),
    (r'^get_self_title/', get_self_title),
)
