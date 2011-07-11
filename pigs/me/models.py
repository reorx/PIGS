#coding=utf-8
import time
import datetime
from hashlib import md5
from django.db.models.base import Model
from django.db.models import *
from django.db import IntegrityError
from django.contrib.auth.models import User
from utils.hashFN import RandomNid
'''
TM: time
CT: count
RI: resource identfication
TG: tag # tag.models
NT: note # note.models
'''
class TM_Model(Model):
    """
    only model templates have no relation with existing apps can be defined in me.models
    """
    created_time = DateTimeField(auto_now_add=True)
    updated_time = DateTimeField()
    def __unicode__(self):
        return 'time model'
    class Meta:
        abstract = True
    def set_updated_time(self):
        self.updated_time = datetime.datetime.now()

class BaseModel(Model):
    md5id = CharField(max_length=32, null=True, unique=True)
    nid = CharField(max_length=8, null=True, unique=True)
    ##
    created_time = DateTimeField(auto_now_add=True)
    updated_time = DateTimeField()

    def __unicode__(self):
        return 'basic model'
    class Meta:
        abstract = True
    def set_updated_time(self):
        self.updated_time = datetime.datetime.now()
    def set_nid(self):
        """
        without .save()
        """
        def try_to_set():
            nid = RandomNid(self.id)
            try:
                self._default_manager.get(nid=nid)
                return False
            except:
                self.nid = nid
                return True
        retn = try_to_set()
        while not retn:
            retn = try_to_set()
    def set_md5id(self):
        s = self.__class__.__name__ + self.nid + str(time.time())
        self.md5id = md5(s).hexdigest()
    @classmethod
    def by_id(cls, id):
        try:
            data = cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None
        return data
    @classmethod
    def by_nid(cls, nid):
        try:
            data = cls.objects.get(nid=nid)
        except cls.DoesNotExist:
            return None
        return data



class UserProfile(BaseModel):
    user = ForeignKey(User, unique=True) # same as OneToOneField
    nickname = CharField(max_length=32)
    bio = CharField(max_length=256)
    def __unicode__(self):
        return 'user profile'
    class Meta:
        db_table = 'user_profile'

class UserSettings(BaseModel):
    user = ForeignKey(User, unique=True) # same as OneToOneField
    knowledge_public = BooleanField(default=False)
    def __unicode__(self):
        return 'user settings'
    class Meta:
        db_table = 'user_settings'
