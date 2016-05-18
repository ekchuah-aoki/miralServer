# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.SalonKind import SalonKind

class BeauticianReviewKind(BaseKind):
    u"""美容師レビュー情報"""
    accountId = ndb.StringProperty()                       #アカウント Id

    rvSalonKey = ndb.KeyProperty(kind=SalonKind)                    #レビューサロンKey
    evaluation = ndb.StringProperty()                                 #評価
    review = ndb.StringProperty()                                     #レビューコメント
