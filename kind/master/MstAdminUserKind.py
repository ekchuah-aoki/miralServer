# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class MstAdminUserKind(BaseKind):
    u"""システム利用ユーザー情報"""
    id = ndb.StringProperty(indexed=True)       #社員番号
    name = ndb.StringProperty()                 #社員名
    

