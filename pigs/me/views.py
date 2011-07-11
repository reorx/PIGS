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

def cate_home(req, tpl='know/cate_home.html'):
    cdic = {}
    cdic['categorys'] = know_QS.categorys()
    return render_tpl(req, tpl, cdic)

def cate_read(req, nid=None, tpl='know/cate.html'):
    qs = know_QS.category(nid)
    if qs is None:
        raise Http404
    cdic = dict(
        category = qs
    )
    return render_tpl(req, tpl, cdic)

def cate_write_create(req, tpl='know/cate_write_create.html'):
    if 'GET' == req.method:
        cdic = dict(
            form = CategoryForm()
        )
        return render_tpl(req, tpl, cdic)
    if 'POST' == req.method:
        form = CategoryForm(data=req.POST)
        if not form.is_valid():
            cdic = dict(
                form = form
            )
            return render_tpl(req, tpl, cdic)
        form.save()
        return HttpResponseRedirect('/know/category/')
    return HttpResponse('405 method error')

def cate_write_modify(req, nid=None, tpl='know/cate_write_modify.html'):
    qs = know_QS.category(nid)
    if qs is None:
        raise Http404
    if 'GET' == req.method:
        cmd_delete = req.GET.get('delete')
        if str(1) == cmd_delete:
            qs.delete()
            return HttpResponseRedirect('/know/category/')
        cdic = dict(
            form = CategoryForm(instance=qs)
        )
        return render_tpl(req, tpl, cdic)
    if 'POST' == req.method:
        form = CategoryForm(data=req.POST, instance=qs)
        if not form.is_valid():
            cdic = dict(
                form = form
            )
            return render_tpl(req, tpl, cdic)
        form.save()
        return HttpResponseRedirect('/know/category/')
    return HttpResponse('405 method error')

def know_home(req, tpl='know/home.html'):
    cdic = {}
    cdic['knows'] = know_QS.knows()
    return render_tpl(req, tpl, cdic)

def know_read(req, nid=None, tpl='know/know.html'):
    """
    preparing rules for api:
        when GET, args are:
            - nid - with_child    (0, 1)
            - data_type          'json','html'[default]
            - c_id
        well, POST not allow
    """
    qs = know_QS.know(nid)
    if qs is None:
        raise Http404
    cdic = dict(
        know = qs
    )
    return render_tpl(req, tpl, cdic)

def know_write_create(req, tpl='know/know_write_create.html'):
    if 'GET' == req.method:
        cdic = dict(
            form = KnowForm()
        )
        return render_tpl(req, tpl, cdic)
    if 'POST' == req.method:
        form = KnowForm(data=req.POST)
        if not form.is_valid():
            cdic = dict(
                form = form
            )
            return render_tpl(req, tpl, cdic)
        form.save()
        return HttpResponseRedirect('/know/')
    return HttpResponse('405 method error')

def know_write_modify(req, nid=None, tpl='know/know_write_modify.html'):
    qs = know_QS.know(nid)
    print qs
    print dir(qs)
    print qs.brief
    if qs is None:
        raise Http404
    if 'GET' == req.method:
        cdic = dict(
            form = KnowForm(instance=qs),
            form_ins = qs
        )
        return render_tpl(req, tpl, cdic)
    return HttpResponse('405 method error')
