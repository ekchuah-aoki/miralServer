# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.ImageKind import ImageKind

class SalonGalleryKind(BaseKind):
    u"""サロンプロフィール画像情報"""
    imageKey = ndb.KeyProperty(kind=ImageKind)                        #画像Key
    thImageKey = ndb.KeyProperty(kind=ImageKind)                      #サムネイル画像Key
    caption = ndb.StringProperty()                                    #キャプション
