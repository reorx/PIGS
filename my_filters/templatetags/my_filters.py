#coding=utf-8

from django import template
from django.utils.encoding import force_unicode
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def numRise(value, r):
    return str(int(value) + int(r))

@register.filter
@stringfilter
def numFall(value, r):
    return str(int(value) - int(r))


# before
@register.filter
@stringfilter
def truncatefilter(value, num):
    try:
        length = int(num)
    except ValeError:
        return value
    unicode_value = force_unicode(value)
    if length < unicode_value.__len__():
        value = unicode_value[:length] + '...'
    else:
        value = unicode_value
    return value
truncatefilter.is_safe = True

