import os
import sys
import time
import urllib
import httplib

class SDict(dict):
    """
    Copy from web.utils.Stroage
    Usage:
        >>> o = Storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
    """
    def __init__(self, dic=None):
        if dic:
            for k in dic.keys():
                self.__setattr__(k, dic[k])
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            #raise AttributeError, k
            return None
    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k
    def __repr__(self):
        return '<Storage> ' + dict.__repr__(self)
    def out(self):
        dic = {}
        for k in self.keys():
            dic[k] = self[k]
        return dic

def urlfetch(domain, url, secure=True):
    if secure:
        conn = httplib.HTTPSConnection(domain)
    else:
        conn = httplib.HTTPConnection(domain)
    conn.request('GET', url)
    resp = conn.getresponse()
    return resp.read()

def ins2dic(obj, exclude=None):
    SubDic = obj.__dict__
    for k in SubDic.keys():
        if '_' == k[0]:
            try:
                del SubDic[k]
            except:
                print 'no that key'
    if exclude:
        for k in exclude:
            if k in SubDic.keys():
                del SubDic[k]
    return SubDic

def get_timestamp(s, source=None):
    """
    return float type timestamp
    """
    if 'tw' == source:
        tupletime = time.strptime(s, '%a %b %d %H:%M:%S +0000 %Y')
        #time.strftime('%Y-%m-%d %a %H:%M:%S', tupletime)
        return time.mktime(tupletime)
    if 'fb' == source:
        tupletime = time.strptime(s, '%Y-%m-%dT%H:%M:%S+0000')
        return time.mktime(tupletime)
    raise ValueError
