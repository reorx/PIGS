from utils.view_dependence import *

@login_required
def Entrance(request, tpl='me/home.html'):
    return render_tpl(request, tpl)

@login_required
def c_c_f(request, tpl='ajax/c_c_f.html'):
    return render_tpl(request, tpl)
