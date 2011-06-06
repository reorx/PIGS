from django.shortcuts import render_to_response
######
# from my_PIGS.default.knowledge #
######
from my_PIGS.default.knowledge.query.get import blog_all
from my_PIGS.utils import fn

def home(request,p=0,template_name='blog/home.html'):
    # blog_all blog_list
    # blog_full blog_title
    blogs = blog_all()
    page_limit = 3
    blog_thispage , page = fn.pageSplit(blogs,page_limit,int(p))
    return render_to_response(template_name,{
        'blogs' : blog_thispage,
        #'blogs' : blogs,
        'page' : page,
        }
    )
