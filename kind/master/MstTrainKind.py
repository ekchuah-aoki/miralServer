# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind  import BaseKind

class MstTrainKind(BaseKind):
    u"""路線マスタ"""
    trainCd = ndb.IntegerProperty(indexed=True)                         #路線コード
    trainCompanyCd = ndb.IntegerProperty()                            #路線会社コード
    trainName   = ndb.StringProperty()                                #路線名
    trainNameKana = ndb.StringProperty()                              #路線名カナ
    displayOrder = ndb.IntegerProperty()                              #表示順

