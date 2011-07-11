#coding=utf-8
import time, datetime
from hashlib import md5
from django.db.models.base import Model
from django.db.models import *
from django.contrib.auth.models import User

from me.models import BaseModel
#Knowledge in main
class Knowledge(BaseModel):
    """
    other attrs:
    nid, category, content(or segments), tip(s)
    """
    user = ForeignKey(User, related_name='_knowledges', null=True)
    category = ForeignKey('Category', related_name='_knowledges', null=True)
    name = CharField(max_length=64, null=False, unique=True)
    brief = TextField(null=False)
    # refer #
    refer_object = CharField(max_length=64, null=True)
    refer_md5id = CharField(max_length=32, null=True)
    # spec #
    father_nid = CharField(max_length=8, null=True) # father & son

    def __unicode__(self):
        return self.nid + ': ' + self.name
    class Meta:
        db_table = 'knowledge'
        verbose_name = u'Knowledge'
        verbose_name_plural = u'Knowledges'
    def save(self, *args, **kwargs):
        self.set_updated_time()
        super(Knowledge, self).save(*args, **kwargs)
        if not self.nid:
            self.set_nid()
        if not self.md5id:
            self.set_md5id()
        return super(Knowledge, self).save(*args, **kwargs)

class Category(BaseModel):
    name = CharField(max_length=64, unique=True, null=False)
    description = TextField(null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'category'
        verbose_name = u'Category'
        verbose_name_plural = u'Categorys'
    def save(self, *args, **kwargs):
        self.set_updated_time()
        super(Category, self).save(*args, **kwargs)
        if not self.nid:
            self.set_nid()
        if not self.md5id:
            self.set_md5id()
        return super(Category, self).save(*args, **kwargs)

class Segment(BaseModel):
    knowledge = ForeignKey('Knowledge', related_name='_segments', null=False)
    content = TextField(null=False)

    def __unicode__(self):
        return self.content[:10]
    class Meta:
        db_table = 'segment'
        verbose_name = u'segment'
        verbose_name_plural = u'segment'
    def save(self, *args, **kwargs):
        super(Segment, self).save(*args, **kwargs)
        if not self.nid:
            self.set_nid()
        if not self.md5id:
            self.set_md5id()
        return super(Segment, self).save(*args, **kwargs)
