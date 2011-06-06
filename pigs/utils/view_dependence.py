from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from utils.render import render_tpl, render_api
