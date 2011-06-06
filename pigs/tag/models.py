from django.db.models.base import Model
from django.db.models import *

class Tag(Model):
    _object = CharField(max_length=128, db_index=True)
    name = CharField(max_length=50, db_index=True, unique=True)
    create_time = DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'tag'
    def is_exist(self):
        try:
            t = Tag.objects.get(_object=self._object, name=self.name)
        except:
            return False
        return t

class ObjectTag(Model):
    _object = CharField(max_length=128, db_index=True)
    object_md5id = CharField(max_length=32, db_index=True)
    tag_name = CharField(max_length=50, db_index=True)
    def __unicode__(self):
        return 'ObjectTag'
    class Meta:
        db_table = 'object_tag'
    def is_exist(self):
        try:
            ot = ObjectTag.objects.get(object_md5id=self.object_md5id, tag_name=self.tag_name)
        except:
            return False
        return ot
    def connect(self):
        t = Tag(_object=self._object, name=self.tag_name)
        if not t.is_exist():
            t.save()
        self.save()
    def disconnect(self):
        self.delete()
        return True
    @classmethod
    def give_tags(cls, obj, detail=False):
        qset = cls.objects.filter(object_md5id=obj.md5id)
        obj.tags = None
        if qset:
            obj.tags = qset.values_list('tag_name', flat=True)
            print 'obj tags',obj.tags
        return obj
