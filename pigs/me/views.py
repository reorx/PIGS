from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from utils.render import render_tpl, render_api

@login_required
def Entrance(request, tpl='me/home.html'):
    return render_tpl(request, tpl)

@login_required
def c_c_f(request, tpl='ajax/c_c_f.html'):
    return render_tpl(request, tpl)
