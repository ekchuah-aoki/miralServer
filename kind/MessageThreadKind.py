# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.AccountKind import AccountKind
from kind.MatchingKind import MatchingKind

class MessageThreadKind(BaseKind):
    u"""メッセージスレッド情報"""
    msgType = ndb.IntegerProperty()                                   #メッセージ種別
    caption = ndb.StringProperty()                                    #キャプション
    senderKey = ndb.KeyProperty(kind=AccountKind)                      #初回の発信者（アカウントKey）
    receiverKey = ndb.KeyProperty(kind=AccountKind)                    #初回の受信者（アカウントKey）
    matchingKey = ndb.KeyProperty(kind=MatchingKind)                    #マッチングキー
