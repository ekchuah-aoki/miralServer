# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class BeauticianLicenseKind(BaseKind):
    u"""美容師免許"""
    accountKey = ndb.KeyProperty("kind=AccountKind")                  #アカウントKey
    authReqDate = ndb.DateTimeProperty()                              #承認依頼日
    authDate = ndb.DateProperty()                                     #承認日
    userKey = ndb.KeyProperty("kind=MstAdminUserKind")                #承認ユーザKey
    imageData = ndb.KeyProperty("kind=ImageKind")                     #画像ID
    thImageData = ndb.KeyProperty("kind=ImageKind")                   #サムネイル画像ID
