import string
import time
#import datetime
from random import choice
from hashlib import md5


from django.utils.http import int_to_base36
from django.utils.encoding import smart_str
from django.utils.hashcompat import sha_constructor

seq = string.letters + string.digits

def RandomHash(length=8, chars=seq):
    return ''.join([choice(chars) for i in range(length)])

def TimeHash(length=8, chars=seq):
    result = int_to_base36(int(time.time()))
    if len(result) >= length:
        return result[:length]
    result += RandomHash(length - len(result))
    return result

def RandomNid(user_id, chars=string.digits):
    LIMIT = 9
    RANGE = 5
    #prefix = ''.join([choice(chars) for i in range(5)])
    prefix = ''
    for i in range(RANGE):
        prefix += choice(chars)
    return prefix + '0'*(LIMIT-RANGE-len(str(user_id))) + str(user_id)

def create_password(raw):
    salt = RandomHash(8)
    raw = smart_str(raw)
    hsh = sha_constructor(salt + raw).hexdigest()
    return '%s$%s' % (salt, hsh)

def check_password(raw, enc):
    salt, hsh = enc.split('$')
    raw = smart_str(raw)
    return hsh == sha_constructor(salt + raw).hexdigest()

def ge_md5(s):
    if not isinstance(s, str):
        s = s.encode('utf-8')
    return md5(s).hexdigest()

def create_chooses_token(usign):
    return md5(usign + '_chooses_token').hexdigest()
