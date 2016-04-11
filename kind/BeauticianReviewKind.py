# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class BeauticianReviewKind(BaseKind):
    u"""美容師レビュー情報"""
    beautiKey = ndb.KeyProperty(index=True,"BeauticianKind")          #美容師Key
    rvSalonKey = ndb.KeyProperty("kind=SalonKind")                    #レビューサロンKey
    evaluation = ndb.StringProperty()                                 #評価
    review = ndb.StringProperty()                                     #レビューコメント
