from google.appengine.ext import ndb
from kind import BaseKind

class MstAdminUserKind(BaseKind):
    """システム利用ユーザー情報"""
    id = ndb.StringProperty(indexed=True)       #社員番号
    name = ndb.StringProperty()                 #社員名
    

