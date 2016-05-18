# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class SalonFacilityKind(BaseKind):
    u"""サロン貸出機材"""
    equipmentId = ndb.StringProperty()                                #機材ID
