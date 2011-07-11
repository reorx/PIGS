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
from knowledge import QS as know_QS

jdic = {'code':404,'message':'Not Found','data':None}

@only_get
@login_required
def ReadKnow(request):
    """
    when GET, args are:
        - nid - with_child    (0, 1)
        - data_type           'json','html'[default]
        - c_id                category id
    well, POST not allow
    """

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
        edic = _dic(data)
        c = KnowledgeCategory(**edic)
        st = c.save()
        if not st:
            jdic['code'] = 303
            jdic['message'] = 'save error'
            return jdic
        jdic['code'] = 200
        jdic['message'] = 'save ok'
        return render_json(request, jdic)

        #if not data or not action:
            #raise Http404
    if 'DELETE' == request.method:
        return HttpResponse('delete')
    return HttpResponse('failed')
