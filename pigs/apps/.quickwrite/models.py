###########
## extra ##
###########
#quick write
class Quickwrite(BasicModel):
    content = TextField(null=False)

    def __unicode__(self):
        return self.content[:10]
    class Meta:
        db_table = 'quickwrite'
        verbose_name = u'Quickwrite'
        verbose_name_plural = u'Qws'
