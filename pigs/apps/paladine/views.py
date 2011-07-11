#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required


def site_entrance(request, tpl='me/home.html'):
    return render_tpl(request, tpl)
