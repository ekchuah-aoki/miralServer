# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class BeauticianWorkGalleryKind(BaseKind):
    u"""美容師実績画像情報"""
    beautiKey = ndb.KeyProperty(index=True,"kind=BeauticianKind")     #美容師Key
    displayOrder = ndb.StringProperty()                               #表示順
    imageKey = ndb.KeyProperty("kind=ImageKind")                      #画像Key
    thImageKey = ndb.KeyProperty("kind=ImageKind")                    #サムネイル画像Key
    caption = ndb.StringProperty()                                    #キャプション
