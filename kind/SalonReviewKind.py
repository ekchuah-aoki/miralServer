
from google.appengine.ext import ndb
from kind import BaseKind

class SalonReviewKind(BaseKind):
    """サロンレビュー情報"""
    salonKey = ndb.KeyProperty(index=True,"Kind=SalonKind")           #サロンKey
    rvBeautiKey = ndb.KeyProperty()                                   #レビュー美容師Key
    evaluation = ndb.FloatProperty()                                  #評価
    review = ndb.TextProperty()                                       #レビューコメント
