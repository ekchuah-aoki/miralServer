# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.AccountKind import AccountKind

class MatchingKind(BaseKind):
    u"""マッチング情報"""
    beautiKey = ndb.KeyProperty(kind=AccountKind)                  #美容師のアカウントKey
    salonKey = ndb.KeyProperty(kind=AccountKind)                   #サロンのアカウントKey
    reqDirect = ndb.IntegerProperty()                                 #依頼方向
    reqTime = ndb.DateTimeProperty()                                  #依頼日時
    status = ndb.IntegerProperty()                                    #ステータス
    matchingTime = ndb.DateTimeProperty()                             #マッチング日時
    favorite = ndb.BooleanProperty()                                  #お気に入り
