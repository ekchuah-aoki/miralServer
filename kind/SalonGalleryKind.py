# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class SalonGalleryKind(BaseKind):
    u"""サロンプロフィール画像情報"""
    salonKey = ndb.KeyProperty(index=True,"Kind=SalonKind")           #サロンKey
    displayOrder = ndb.IntegerProperty()                              #表示順
    imageKey = ndb.KeyProperty("kind=ImageKind")                     #画像Key
    thImageKey = ndb.KeyProperty("kind=ImageKind")                   #サムネイル画像Key
    caption = ndb.StringProperty()                                    #キャプション
