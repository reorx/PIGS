#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.template import RequestContext,Context
from django.template.loader import get_template
#from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from utils.render import render_tpl, render_json, render_api
from utils.decorators import only_get
from utils.json import _dic, _json

from knowledge.models import Knowledge, KnowledgeCategory, KnowledgeSegment

@only_get
@login_required
def ReadKnow(request):
    """
    when GET, args are:
        - nid - with_child    (0, 1)
        - data_type          'json','html'[default]
        - c_id
    well, POST not allow
    """
    if 'GET' != request.method:
        raise Http404
    # args init #
    nid = request.GET.get('nid', None)
    with_child = request.GET.get('with_child',None)
    data_type = request.GET.get('data_type', 'html')
    c_id = request.GET.get('c_id', None)
    try:
        c_id = int(c_id)
    except:
        c_id = None
    jdic = {'code':404,'message':'Not Found','data':None}

    if not nid:
        if data_type == 'html':
            return render_tpl(request, 'me/know.html')
        if data_type == 'json':
            if c_id:
                ctgr = KnowldegeCategory.by_id(c_id)
            return render_json(request, jdic)
    know = Knowledge.by_nid(nid)
    if not know:
        raise Http404
    if data_type == 'html':
        return render_tpl(request, 'me/know.html')
    if data_type == 'json':
        jdic['data']
        return render_json(request, jdic)
    return HttpResponse('failed')

@login_required
def WriteKnow(request):
    """
    action: create, update, delete
    if 'POST' == request.method:
        action = request.POST.get('action', None)
        data = request.POST.get('data', None)
        if not action or not data:
            raise Http404
        if 'create' == action:
        if 'update' == action:
    if 'DELETE' == request.method:
    """
    return HttpResponse('method not allowed')

@only_get
def ReadKnowCategory(request):
    jdic = {'code':404,'message':'Not Found','data':None}
    return render_json(request, jdic)

def WriteKnowCategory(request):
    if 'POST' == request.method:
        action = request.POST.get('action', None)
        data = request.POST.get('data', None)
        print data
        jdic = _dic(data)
        print jdic
        c = KnowledgeCategory(**jdic)
        c.save()
        #if not data or not action:
            #raise Http404
        return HttpResponse('skdj')
    if 'DELETE' == request.method:
        return HttpResponse('delete')
    return HttpResponse('failed')
