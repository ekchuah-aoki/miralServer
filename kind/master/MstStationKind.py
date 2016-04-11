
from google.appengine.ext import ndb
from kind import BaseKind

class MstStationKind(BaseKind):
    """路線駅マスタ"""
    stationCd = ndb.IntegerProperty(index=True)                       #駅コード
    name = ndb.StringProperty()                                       #駅名
    nameKana = ndb.StringProperty()                                   #駅名カナ
    trainCd = ndb.IntegerProperty(index=True)                         #路線コード
    displayOrder = ndb.IntegerProperty()                              #表示順
    geoCd = ndb.GeoPtProperty()                                       #緯度・軽度

