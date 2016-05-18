# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class SalonExpendableKind(BaseKind):
    u"""サロン消耗品"""
    name = ndb.StringProperty()                                       #消耗品名
    displayOrder = ndb.IntegerProperty()                              #表示順
    quantity = ndb.StringProperty()                                   #基準数量
    minimumAmount = ndb.IntegerProperty()                             #最低金額
    highsetAmount = ndb.IntegerProperty()                             #最高金額
