# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class SalonGalleryKind(BaseKind):
    u"""サロンプロフィール画像情報"""
    salonKey = ndb.KeyProperty(index=True,"Kind=SalonKind")           #サロンKey
    displayOrder = ndb.IntegerProperty()                              #表示順
    imageId = ndb.StringProperty()                                    #画像ID
    caption = ndb.StringProperty()                                    #キャプション
