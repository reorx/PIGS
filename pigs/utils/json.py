try:
    import cjson as json # cjson is more effective
except ImportError:
    from django.utils import simplejson as json

class DateTimeJSONEncoder(json.JSONEncoder):
    """
    copy from django.core.serializers.json
    """
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%s %s" % (self.DATE_FORMAT, self.TIME_FORMAT))
        elif isinstance(o, datetime.date):
            return o.strftime(self.DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(self.TIME_FORMAT)
        else:
            return super(DateTimeJSONEncoder, self).default(o)

def dumps(o, **kwargs):
    return json.dumps(o, ensure_ascii=False,cls=DateTimeJSONEncoder, **kwargs)

def _dic(json_data):
    return json.loads(json_data)

def _json(dic_data):
    return dumps(dic_data)
