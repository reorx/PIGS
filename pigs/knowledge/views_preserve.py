#coding=utf-8
from django.shortcuts import render_to_response

#from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext,Context
#from django.template.loader import get_template
#from django.contrib.auth.decorators import permission_required

from my_PIGS.default.models import TimeInfo,Category,Knowledge,Tip,Quickwrite
def home(request):
    _test = Knowledge.objects.all()
    t = []
    for test in _test:
        _p = test.parents.all()
        for p in _p:
            t.append((p.title + '||'))
    return render_to_response('home/index.html',{
            'tests' : t,
        },
        context_instance=RequestContext(request)
    )
