# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class SalonExpendableKind(BaseKind):
    u"""サロン消耗品"""
    salonKey = ndb.KeyProperty(index=True,"Kind=SalonKind")           #サロンKey
    name = ndb.StringProperty()                                       #消耗品名
    displayOrder = ndb.IntegerProperty()                              #表示順
    minimumAmount = ndb.IntegerProperty()                             #最低金額
    highsetAmount = ndb.IntegerProperty()                             #最高金額
