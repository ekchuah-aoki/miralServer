# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class SalonFacilityKind(BaseKind):
    u"""サロン貸出機材"""
    salonKey = ndb.KeyProperty(index=True,"Kind=SalonKind")           #サロンKey
    equipmentId = ndb.StringProperty()                                #機材ID
