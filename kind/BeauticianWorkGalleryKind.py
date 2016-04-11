# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class BeauticianWorkGalleryKind(BaseKind):
    u"""美容師実績画像情報"""
    beautiKey = ndb.KeyProperty(index=True,"kind=BeauticianKind")     #美容師Key
    displayOrder = ndb.StringProperty()                               #表示順
    imageId = ndb.StringProperty()                                    #画像ID
    caption = ndb.StringProperty()                                    #キャプション
