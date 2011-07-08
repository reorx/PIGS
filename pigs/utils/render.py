from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.utils import simplejson

class DateTimeJSONEncoder(simplejson.JSONEncoder):
    """
    copy from django.core.serializers.json
    """
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%s %s" % (self.DATE_FORMAT, self.TIME_FORMAT))
        elif isinstance(o, datetime.date):
            return o.strftime(self.DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(self.TIME_FORMAT)
        else:
            return super(DateTimeJSONEncoder, self).default(o)

def dumps(o, **kwargs):
    return simplejson.dumps(o, ensure_ascii=False,cls=DateTimeJSONEncoder, **kwargs)

def render_tpl(request, tpl, cdic={}):
    cdic['request'] = request
    return render_to_response(
        tpl,
        cdic,
        #context_instance=RequestContext(request)
    )

def render_json(request, dic):
    json = dumps(dic)
    return HttpResponse(json, content_type='application/json')

def render_api(request, dic):
    json = dumps(dic)
    return HttpResponse(json, content_type='application/json')
