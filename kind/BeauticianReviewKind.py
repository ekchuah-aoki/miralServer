# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.BeauticianKind import BeauticianKind
from kind.SalonKind import SalonKind

class BeauticianReviewKind(BaseKind):
    u"""美容師レビュー情報"""
    beautiKey = ndb.KeyProperty(indexed=True,kind=BeauticianKind)          #美容師Key
    rvSalonKey = ndb.KeyProperty(kind=SalonKind)                    #レビューサロンKey
    evaluation = ndb.StringProperty()                                 #評価
    review = ndb.StringProperty()                                     #レビューコメント
