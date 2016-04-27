# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind  import BaseKind

class MstTrainCampanyKind(BaseKind):
    u"""路線マスタ"""
    campanyCd = ndb.IntegerProperty(indexed=True)                       #路線事業者コード
    companyNama = ndb.StringProperty()                                 #路線事業者名コード
    companyNameKana = ndb.StringProperty()                              #路線事業者名カナ
    displayOrder = ndb.IntegerProperty()                                #表示順

