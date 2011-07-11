from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import urlquote

class only_method:
    def __init__(self, method):
        self.method = method
    def __call__(self, fn, *args, **kwargs):
        def _wrapper(request, *args, **kwargs):
            if self.method == request.method:
                return fn(request, *args, **kwargs)
            response = HttpResponse('Method Not Allowed')
            response.status_code = 405
            return response
        return _wrapper

def not_mobile(fn):
    def _wrapper(request, *args, **kwargs):
        if request.is_mobile:
            return HttpResponseRedirect('/m/')
        return fn(request, *args, **kwargs)
    return _wrapper
