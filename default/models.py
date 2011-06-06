#coding=utf-8
from django.db import models
import datetime

##########
## base ##
##########

class TimeInfo(models.Model):
    dtime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.dtime

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categorys'

class ContentNote(TimeInfo):
    content = models.TextField(null=False)

    def __unicode__(self):
        return u'%s' %(self.id)

class ContentPart(TimeInfo):
    content = models.TextField(null=False)
    notes = models.ManyToManyField(ContentNote, related_name='inContent', null=True, blank=True)

    def __unicode__(self):
        return u'%s' %(self.id)

    class Meta:
        verbose_name = u'ContentPart'
        verbose_name_plural = u'Contents'

class Refer(models.Model):
    resource_name = models.CharField(max_length=50, null=True, blank=True)
    resource_id = models.IntegerField()

    def __unicode__(self):
        return u'%s' %(self.id)

    class Meta:
        verbose_name = u'Refer'
        verbose_name_plural = u'Refers'
##########
## main ##
##########

#Knowledge in main
class Knowledge(TimeInfo):
    category = models.ForeignKey(Category, null=False)
    title = models.CharField(max_length=50, null=False)
    brief = models.TextField(null=False)
    contents = models.ManyToManyField(ContentPart, related_name='inKnowledge',null=True, blank=True)
    # extend #
    refer = models.ForeignKey(Refer, null=True, blank=True)
    parent = models.ManyToManyField('self', related_name='itsChildren', symmetrical=False, null=True, blank=True)
    ## of no use
    #content = models.TextField(null=False)
    #brothers = models.ManyToManyField('self', related_name='itsBrothers', null=True, blank=True)
    #tips = models.ManyToManyField(Tip, related_name='inKnowledge', null=True, blank=True)

    def __unicode__(self):
        return (self.category.name + ':' + str(self.id))

    class Meta:
        verbose_name = u'Knowledge'
        verbose_name_plural = u'Knowledges'
        #permissions = (
            #('can_arrange', 'can arrange'),
        #)

###########
## extra ##
###########

#quick write
class Quickwrite(TimeInfo):
    content = models.TextField(null=False)

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name = u'Quickwrite'
        verbose_name_plural = u'QWs'
        #permissions = (
            #('can_arrange', 'can arrange'),
        #)


