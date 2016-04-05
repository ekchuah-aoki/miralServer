
from google.appengine.ext import ndb
from kind import BaseKind

class SalonFacilityKind(BaseKind):
    """サロン貸出機材"""
    salonKey = ndb.KeyProperty(index=True,"Kind=SalonKind")           #サロンKey
    equipmentId = ndb.StringProperty()                                #機材ID
