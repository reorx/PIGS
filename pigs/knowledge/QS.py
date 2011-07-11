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

def know(nid,
        with_refer=True,
        with_children=True,
        children_with_refer=True):
    def add_segments(k):
        k.segments = k._segments.all()
        return k
    def add_refer(k):
        if k.refer_md5id and k.refer_object:
            pass
        return k
    def add_children(k):
        k.children = [add_segments(i) for i in KM.filter(father_nid=nid)]
        return k
    ##
    try:
        k = KM.get(nid=nid)
    except Knowledge.DoesNotExist:
        return None
    k = add_segments(k) # segments added
    if with_refer: # refer adding
        k = add_refer(k)
    if with_children: # children adding
        k = add_children(k)
    return k

def knows(c_id=None):
    if c_id:
        try:
            category = CM.get(id=c_id)
        except Category.DoesNotExist:
            return None
        knows = KM.filter(category=category)
        return knows # could be None
    else:
        #TODO tree structure knows
        return KM.all()

def category(nid):
    try:
        category = CM.get(nid=nid)
    except Category.DoesNotExist:
        return None
    return category

def categorys():
    return CM.all()
