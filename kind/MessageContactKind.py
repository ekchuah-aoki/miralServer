# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class MessageContactKind(BaseKind):
    u"""メッセージコンタクト情報情報"""
    messageKey = ndb.KeyProperty("kind=MessageThreadKind")           #メッセージスレッドKey
    senderType = ndb.IntegerProperty()                               #送信者（美容師、サロン）
    comment = ndb.TextProperty()                                     #コメント
    readTime = ndb.DateTimeProperty()                                #既読日時
      
    