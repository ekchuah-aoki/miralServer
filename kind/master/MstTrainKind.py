
from google.appengine.ext import ndb
from kind import BaseKind

class MstTrainKind(BaseKind):
    """路線マスタ"""
    trainCd = ndb.IntegerProperty(index=True)                         #路線コード
    trainCompanyCd = ndb.IntegerProperty()                            #路線会社コード
    trainNameCd = ndb.StringProperty()                                #路線名
    trainNameKana = ndb.StringProperty()                              #路線名カナ
    displayOrder = ndb.IntegerProperty()                              #表示順

