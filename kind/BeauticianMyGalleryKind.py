# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.BeauticianKind import BeauticianKind
from kind.ImageKind import ImageKind


class BeauticianMyGalleryKind(BaseKind):
    u"""美容師プロフィール画像情報"""
    beautiKey = ndb.KeyProperty(indexed=True,kind=BeauticianKind)      #美容師Key
    displayOrder = ndb.IntegerProperty()                              #表示順
    imageKey = ndb.KeyProperty(kind=ImageKind)                     #画像Key
    thImageKey = ndb.KeyProperty(kind=ImageKind)                   #サムネイル画像Key
    caption = ndb.StringProperty()                                    #キャプション
