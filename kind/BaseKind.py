# coding: UTF-8

from google.appengine.ext import ndb
class BaseKind(ndb.Model):
    u"""ベース情報"""
    regUserKey = ndb.KeyProperty(kind='MstAdminUserKind')        #登録者CD
    regDateTime = ndb.DateTimeProperty(auto_now_add=True)           #登録日時
    modUserKey = ndb.KeyProperty(kind='MstAdminUserKind')        #変更者CD
    modDateTime = ndb.DateTimeProperty(auto_now=True)               #変更日時
    delFlg =ndb.BooleanProperty(default=False)                  #削除フラグ

