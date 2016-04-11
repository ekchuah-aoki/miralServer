# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class SalonReviewKind(BaseKind):
    u"""サロンレビュー情報"""
    salonKey = ndb.KeyProperty(index=True,"Kind=SalonKind")           #サロンKey
    rvBeautiKey = ndb.KeyProperty()                                   #レビュー美容師Key
    evaluation = ndb.FloatProperty()                                  #評価
    review = ndb.TextProperty()                                       #レビューコメント
