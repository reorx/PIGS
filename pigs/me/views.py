from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from utils.render import render_tpl, render_json, render_api
from utils.decorators import only_method
from utils.json import _dic, _json
from knowledge.models import Knowledge, Category, Segment
from knowledge import QS as know_QS
from knowledge.forms import CategoryForm, KnowForm

def site_entrance(request, tpl='me/home.html'):
    return render_tpl(request, tpl)

def know_home(req, tpl='know/home.html'):
    return render_tpl(req, tpl)

@only_method('GET')
def know_read(req, nid=None, tpl='know/know.html'):
    """
    when GET, args are:
        - nid - with_child    (0, 1)
        - data_type          'json','html'[default]
        - c_id
    well, POST not allow
    """
    # args init #
    with_child = req.GET.get('with_child',None)
    #data_type = request.GET.get('data_type', 'html')
    # get QuerySet #
    qs = know_QS.know(nid, with_child)
    if qs is None:
        raise Http404
    # responsing #
    cdic = dict(
        know = qs
    )
    return render_tpl(req, tpl, cdic)

@only_method('POST')
def know_write(req):
    pass

def cate_home(req, tpl='know/cate_home.html'):
    form = CategoryForm()
    cdic = {'form': form}
    return render_tpl(req, tpl, cdic)

def cate_read(req):
    pass

@only_method('POST')
def cate_write_create(req):
    print req.POST
    form = CategoryForm(data=req.POST)
    if not form.is_valid():
        print 'not valid'
        cdic = dict(
            form = form
        )
        return render_tpl(req, 'know/cate_home.html', cdic)
    print 'is valid'
    print dir(form)
    form.save()
    return HttpResponseRedirect('/know/category/')

def cate_write_modify(req):
    pass
