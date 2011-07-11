from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext,Context
from django.template.loader import get_template

from utils.tools import SDict, ins2dic, get_timestamp
from utils.json import _dic, _json

def _render_tpl(tpl_name, cdic={}):
    tpl = get_template(tpl_name)
    context = Context(cdic)
    return tpl.render(context)

def render_tpl(request, tpl, cdic={}):
    cdic['request'] = request
    return render_to_response(
        tpl,
        cdic,
        #context_instance=RequestContext(request)
    )

def render_json(request, dic):
    json = _json(dic)
    return HttpResponse(json, content_type='application/json')

def render_api(req, status=None, msg=None, data=None):
    stSD = SDict({'status': 99,'msg':'Not Found', 'data':None})
    stSD.status = status
    stSD.msg = msg
    stSD.data = data
    return render_json(req, stSD.out())

def resp_json(json):
    return HttpResponse(json, content_type='application/json')

