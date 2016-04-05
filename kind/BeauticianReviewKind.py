
from google.appengine.ext import ndb
from kind import BaseKind

class BeauticianReviewKind(BaseKind):
    """美容師レビュー情報"""
    beautiKey = ndb.KeyProperty(index=True,"BeauticianKind")          #美容師Key
    rvSalonKey = ndb.KeyProperty("kind=SalonKind")                    #レビューサロンKey
    evaluation = ndb.StringProperty()                                 #評価
    review = ndb.StringProperty()                                     #レビューコメント
