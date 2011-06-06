#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext,Context
from django.template.loader import get_template
#from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from utils.render import render_tpl, render_api
#from django.contrib.auth.decorators import permission_required

from my_PIGS.default.models import *

# query #
from query import get as get_k
from query import set as set_k

# function #
def ajax_response(t,c):
    t = get_template(t)
    c = Context(c)
    return HttpResponse(t.render(c))

def knowledgeFull(k_id):
    k = get_k.knowledge(k_id)
    k.category_reset = k.category.name
    k.tips_reset = k.tips.all()
    if k.parents.all():
        k.parent_reset = k.parents.all().get()
    else:
        k.parent_reset = ''
    if k.brothers.all():
        k.brother_reset= k.brothers.all().get()
    else:
        k.brother_reset = ''
    return k

def getData(request):
    class d: pass
    d.id =request.POST.get('id') # exist is to change
    d.category_id = request.POST.get('category_id')
    d.title = request.POST.get('title')
    d.brief = request.POST.get('brief')
    d.a_content = request.POST.get('a_content') # to ContentPart
    ##
    d.parent = request.POST.get('parent')
    d.refer = request.POST.get('refer') # exist is to clear relationship
    ####
    return d

# index #
def index(request):
    category_list = get_k.category_all()
    return render_to_response('knowledge/base.html',{
        'category_list': category_list,
        },
        context_instance=RequestContext(request)
    )

# knowledge #
def create_or_change(request):
    print 'in cc'
    d = getData(request)
    #certify = get_k.certify(d)
    ####
    if d.id!='': #change
        print 'change'
        print d.parent
        k_id = set_k.change(d)
    else: #create
        print 'create'
        k_id = set_k.create_basic(d)
    return HttpResponse(k_id)

def delete(request):
    k_id = request.GET.get('knowledge_id')
    return HttpResponse(set_k.delete(k_id))

# page request #
def view_k_list(request):
    c_id= int(request.GET.get('category'))
    t = 'knowledge/infoarea_knowledgelist.html'
    c = {
        'html':get_k.knowledge_category_tree(c_id)
    }
    return (ajax_response(t,c))

def infoarea_category(request):
    c_id= int(request.GET.get('category'))
    category = get_k.category(id=c_id)
    t = 'knowledge/infoarea_category.html'
    c = {
        'category' : category,
    }
    return (ajax_response(t,c))

def content_knowledge(request):
    k_id = int(request.GET.get('knowledge'))
    knowledge = get_k.knowledge_full(k_id)
    t = 'knowledge/content_knowledge.html'
    c = {
        'k' : knowledge,
    }
    return (ajax_response(t,c))

def extend_k_info(request):
    k_id = request.GET.get('k_id')
    k = get_k.knowledge_info(k_id)
    return ajax_response('knowledge/extend_k_info.html',{'k':k})

def editor_contentpart(request):
    t = get_template('knowledge/editor_contentpart.html')
    k_id = request.GET.get('knowledge_id')
    if k_id:
        k = knowledgeFull(k_id)
        c = Context({
            'k':k,
        })
    else:
        c = Context()
    return HttpResponse(t.render(c))

def editor_extendpart(request):
    t = get_template('knowledge/editor_extendpart.html')
    k_id = request.GET.get('knowledge_id')
    mode = request.GET.get('mode')
    if mode == 'edit':
        k = knowledgeFull(k_id)
        c = Context({
            'k':k,
            'mode':mode,
        })
    else: # mode == 'add'
        c = Context({
            'mode':mode,
        })
    return HttpResponse(t.render(c))

def ajax_parent(request):
    c_id = request.GET.get('category')
    t = request.GET.get('title')
    k_id  = request.GET.get('knowledge_id')
    html = ''
    if k_id == '':
        ks = get_k.knowledge_title_search(c_id,t)
    else:
        ks = get_k.knowledge_title_search_nochild(c_id,t,k_id)
    for k in ks:
        html += ('<div class="search_result">'+k.title+'</div>')
    return  HttpResponse(html)

def ajax_certify(request):
    d = getData(request)
    status = get_k.certify(d)
    return HttpResponse(status)

def add_content(request):
    k_id = request.POST.get('k_id')
    print k_id
    a_content = request.POST.get('a_content')
    print a_content
    set_k.add_content(k_id,a_content)
    return HttpResponse('')

def add_tip(request):
    k_id = request.GET.get('knowledge_id')
    c = request.GET.get('content')
    t_id = set_k.add_tip(k_id,c)
    return HttpResponse(t_id)

def change_tip(request):    # include remove
    c = request.GET.get('content')
    t_id = request.GET.get('tip_id')
    if c!='':
        set_k.change_tip(t_id,c)
        status = 'tip changed'
    else:
        set_k.remove_tip(t_id)
        status = 'tip was removed'
    return HttpResponse(status)

def get_parent_title(request):
    k_id = request.GET.get('knowledge_id')
    title = get_k.get_parent_title(k_id)
    return HttpResponse(title)

def get_self_title(request):
    k_id = request.GET.get('knowledge_id')
    title = get_k.get_self_title(k_id)
    return HttpResponse(title)
