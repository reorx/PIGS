from django.db.models.base import Model
from django.db.models import *

class Note(Model):
    name = CharField(max_length=32)
    type = IntegerField()
    def __unicode__(self):
        return 'a note'
    class Meta:
        db_table = 'note'
