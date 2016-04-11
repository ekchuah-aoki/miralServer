# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class BeauticianMyGalleryKind(BaseKind):
    u"""美容師プロフィール画像情報"""
    salonKey = ndb.KeyProperty(index=True,"kind=BeauticianKind")      #美容師Key
    displayOrder = ndb.IntegerProperty()                              #表示順
    imageId = ndb.StringProperty()                                    #画像ID
    caption = ndb.StringProperty()                                    #キャプション
