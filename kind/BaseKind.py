
from google.appengine.ext import ndb
class BaseKind(ndb.Model):
    """ベース情報"""
    regUserKey = ndb.StringProperty(kind='MstAdminUserKind')        #登録者CD
    regDateTime = ndb.DateTimeProperty(auto_now_add=True)           #登録日時
    modUserKey = ndb.StringProperty(kind='MstAdminUserKind')        #変更者CD
    modDateTime = ndb.DateTimeProperty(auto_now=True)               #変更日時

