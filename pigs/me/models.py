#coding=utf-8
import logging
import time, datetime
from hashlib import md5
from django.db.models.base import Model
from django.db.models import *

class BasicModel(Model):
    create_time = DateTimeField(auto_now_add=True)
    md5id = CharField(max_length=32, null=True)
    nid = CharField(max_length=8)

    def __unicode__(self):
        return 'basic model'
    class Meta:
        abstract = True
    def set_nid(self):
        if not self.nid:
            from utils.hashFN import RandomNid
            self.nid = RandomNid(self.id)
    def set_md5id(self):
        if not self.md5id:
            s = self.__class__.__name__ + self.nid + str(time.time())
            self.md5id = md5(s).hexdigest()
    @classmethod
    def by_id(cls, id):
        try:
            data = cls.objects.get(id=id)
        except:
            return None
        return data
    @classmethod
    def by_nid(cls, nid):
        try:
            data = cls.objects.get(nid=nid)
        except cls.DoesNotExist:
            return None
        except cls.MultipleObjectsReturned:
            logging.error('DB Multiple User nid: ' + nid)
            return None
        return data
