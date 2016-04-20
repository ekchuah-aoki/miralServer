# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class BeauticianMyGalleryKind(BaseKind):
    u"""美容師プロフィール画像情報"""
    salonKey = ndb.KeyProperty(indexed=True,"kind=BeauticianKind")      #美容師Key
    displayOrder = ndb.IntegerProperty()                              #表示順
    imageData = ndb.BlobProperty()                                  #画像データ
    caption = ndb.StringProperty()                                    #キャプション
