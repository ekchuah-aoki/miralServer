# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class MessageThreadKind(BaseKind):
    u"""メッセージスレッド情報"""
    msgType = ndb.IntegerProperty()                                    #メッセージ種別
    caption = ndb.StringProperty()                                    #キャプション
    matchingKey = ndb.KeyProperty("kind=MatchingKind")                #マッチングキー
