from django.db.models.base import Model
from django.db.models import *
from django.db import transaction
from me.models import TM_Model

class Tag(TM_Model):
    #obj = ManyToManyField('') # used for relatively indenpent app to conn with other main model objects(idea about MTM)
    name = CharField(max_length=32, db_index=True, unique=True)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'tag'

class ObjTag(TM_Model):
    obj = CharField(max_length=32, db_index=True) # obj's md5id
    tag = ForeignKey('Tag', related_name='in_objs')
    def __unicode__(self):
        return 'Obj Tag'
    class Meta:
        db_table = 'obj_tag'

####
class TG_Model(Model):
    """
    depend on RI_Model
    and is related with Tag & ObjTag models
    so, should be in tag.models
    """
    #_TAG = Tag
    #_ObjTag = ObjTag
    def __unicode__(self):
        return 'time model'
    class Meta:
        abstract = True
    @transaction.commit_manually
    def set_tag(self, name):
        try:
            tag = Tag.objects.get('name')
        except Tag.DoesNotExist:
            tag = Tag(name = name)
            tag.save()

        ot = ObjTag(
            obj = self.md5id,
            tag = tag)
        ot.save()
        transaction.commit()
        return True
    def get_tags(self):
        qs = ObjTag.objects.filter(obj = self.md5id).values_list('tag', flat=True)
        return qs
