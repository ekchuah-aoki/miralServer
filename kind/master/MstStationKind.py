# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class MstStationKind(BaseKind):
    u"""路線駅マスタ"""
    stationCd = ndb.IntegerProperty(indexed=True)                       #駅コード
    stationGpCd = ndb.IntegerProperty(indexed=True)                     #駅グループコード
    stationName = ndb.StringProperty()                                  #駅名
    stationNameKana = ndb.StringProperty()                              #駅名カナ
    trainCd = ndb.IntegerProperty(indexed=True)                         #路線コード
    geoCd = ndb.GeoPtProperty()                                         #緯度・軽度
    displayOrder = ndb.IntegerProperty()                                #表示順

