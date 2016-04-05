
from google.appengine.ext import ndb
from kind import BaseKind

class MessageContactKind(BaseKind):
    """メッセージコンタクト情報情報"""
    messageKey = ndb.KeyProperty("kind=MessageThreadKind")            #メッセージスレッドKey
    sender = ndb.IntegerProperty()                                    #コンタクト方向
    comment = ndb.TextProperty()                                      #コメント
