from utils.hashFN import ge_md5
from django.conf import settings

COOKIE_USER_NID = 'COOKIE_USER_NID'

def GenerateCookieValue(user,origin=None):
    md5word = hashFN.ge_md5(user.nid + user.email)
    if origin:
        if not isinstance(origin, str):
            origin = origin.encode('utf-8')
        cookie = hashFN.ge_md5(md5word + origin)
    return cookie

def SetCookieUserNid(response, user, keep=False):
    if keep:
        response.set_cookie(COOKIE_USER_NID,
            value = GenerateCookieValue(user, 'nid'),
            max_age = settings.SESSION_COOKIE_AGE,
            #max_age = request.session.get_expiry_age(),
            domain = settings.SESSION_COOKIE_DOMAIN
        )
    else:
        response.set_cookie(settings.COOKIE_USER_NID,
            value = GenerateCookieValue(user, 'nid'),
            max_age = None,
            expires = None,
            #max_age = request.session.get_expiry_age(),
            domain = settings.SESSION_COOKIE_DOMAIN
        )
    return response
