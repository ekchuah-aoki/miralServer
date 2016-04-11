
from google.appengine.ext import ndb
from kind import BaseKind

class MessageThreadKind(BaseKind):
    """メッセージスレッド情報"""
    msgType = ndb.IntegerProperty()                                    #メッセージ種別
    caption = ndb.StringProperty()                                    #キャプション
    matchingKey = ndb.KeyProperty("kind=MatchingKind")                #マッチングキー
