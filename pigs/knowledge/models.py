#coding=utf-8
# -*- coding=utf-8 -*-
import logging
import time, datetime
from hashlib import md5
import MySQLdb as DB
from django.db.models.base import Model
from django.db.models import *

from me.models import BasicModel
#Knowledge in main
class Knowledge(BasicModel):
    """
    other attrs:
    nid, category, content(or segments), tip(s)
    """
    u_id = IntegerField() # user id
    c_id = IntegerField() # category id
    father_id = IntegerField() # father knowledge id
    name = CharField(max_length=64)
    brief = TextField()
    # refer #
    refer_object = CharField(max_length=128)
    refer_md5id = CharField(max_length=32)

    def __unicode__(self):
        return self.title + ':' + str(self.id)
    class Meta:
        db_table = 'knowledge'
        verbose_name = u'Knowledge'
        verbose_name_plural = u'Knowledges'
    def save(self):
        super(Knowledge, self).save()
        if not self.nid:
            self.set_nid()
        if not self.md5id:
            self.set_md5id()
        return super(Knowledge, self).save()

class KnowledgeCategory(BasicModel):
    name = CharField(max_length=64, unique=True, null=False)
    intro = TextField(null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'knowledge_category'
        verbose_name = u'Category'
        verbose_name_plural = u'Categorys'
    def save(self):
        try:
            super(KnowledgeCategory, self).save()
            return True
        except:
            print 'save error'
            return False


class KnowledgeSegment(BasicModel):
    k_id = IntegerField()
    content = TextField()

    def __unicode__(self):
        return self.content[:10]
    class Meta:
        db_table = 'knowledge_segment'
        verbose_name = u'segment'
        verbose_name_plural = u'segment'
    def save(self):
        super(KnowledgeSegment, self).save()
        if not self.md5id:
            self.set_md5id()
        return super(KnowledgeSegment, self).save()
