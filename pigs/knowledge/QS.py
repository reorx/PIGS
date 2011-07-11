#coding=utf-8
'''
this module contain functions
which receive args
and return QuerySet instance
without formated data output
'''
from models import *
KM = Knowledge.objects # init model manager
CM = Category.objects

def segment():
    pass

def segments():
    pass

def know(nid, with_child=None):
    def add_segments(k):
        k.segments = k._segments.all()
        return k
    ##
    try:
        know = add_segments(KM.get(nid=nid))
    except Knowledge.DoesNotExist:
        return None
    if with_child:
        know.childs = [add_segments(i) for i in Knowledge.objects.filter(father_nid=nid)]
    return know

def knows(c_id):
    try:
        category = CM.get(id=c_id)
    except Category.DoesNotExist:
        return None
    knows = KM.filter(category=category)
    return knows # could be None

    
    pass

def category():
    pass

def categorys():
    pass
