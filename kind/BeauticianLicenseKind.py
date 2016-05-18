# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.master.MstAdminUserKind import MstAdminUserKind
from kind.ImageKind import ImageKind

class BeauticianLicenseKind(BaseKind):
    u"""美容師免許"""
    authReqDate = ndb.DateTimeProperty()                              #承認依頼日
    authDate = ndb.DateProperty()                                     #承認日
    userKey = ndb.KeyProperty(kind=MstAdminUserKind)                #承認ユーザKey
    imageKey = ndb.KeyProperty(kind=ImageKind)                     #画像Key
    thImageKey = ndb.KeyProperty(kind=ImageKind)                   #サムネイル画像Key
