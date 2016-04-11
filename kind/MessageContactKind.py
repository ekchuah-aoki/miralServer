# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class MessageContactKind(BaseKind):
    u"""メッセージコンタクト情報情報"""
    messageKey = ndb.KeyProperty("kind=MessageThreadKind")            #メッセージスレッドKey
    sender = ndb.IntegerProperty()                                    #コンタクト方向
    comment = ndb.TextProperty()                                      #コメント
