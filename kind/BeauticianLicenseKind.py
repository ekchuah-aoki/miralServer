
from google.appengine.ext import ndb
from kind import BaseKind

class BeauticianLicenseKind(BaseKind):
    """美容師免許"""
    beautiKey = ndb.KeyProperty(index=True,"kind=BeauticianKind")     #美容師Key
    authReqDate = ndb.DateProperty()                                  #承認依頼日
    authDate = ndb.DateProperty()                                     #承認日
    userKey = ndb.KeyProperty("kind=MstAdminUserKind")                #承認ユーザKey
    imageId = ndb.StringProperty()                                    #画像ID
