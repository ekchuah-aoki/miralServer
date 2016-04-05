
from google.appengine.ext import ndb
from kind import BaseKind

class MatchingKind(BaseKind):
    """マッチング情報"""
    beautiKey = ndb.KeyProperty(index=True,"kind=BeauticianKind")     #美容師Key
    salonKey = ndb.KeyProperty(indexed=True)                          #サロンKey
    reqDirect = ndb.IntegerProperty()                                 #依頼方向
    reqTime = ndb.DateTimeProperty()                                  #依頼日時
    status = ndb.IntegerProperty()                                    #ステータス
    matchingTime = ndb.DateTimeProperty()                             #マッチング日時
    favorite = ndb.BooleanProperty()                                  #お気に入り
