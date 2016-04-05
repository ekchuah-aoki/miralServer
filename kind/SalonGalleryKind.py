
from google.appengine.ext import ndb
from kind import BaseKind

class SalonGalleryKind(BaseKind):
    """サロンプロフィール画像情報"""
    salonKey = ndb.KeyProperty(index=True,"Kind=SalonKind")           #サロンKey
    displayOrder = ndb.IntegerProperty()                              #表示順
    imageId = ndb.StringProperty()                                    #画像ID
    caption = ndb.StringProperty()                                    #キャプション
