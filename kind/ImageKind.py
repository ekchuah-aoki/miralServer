# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind 

class ImageKind(BaseKind):
    u"""画像"""
    fileName = ndb.StringProperty()                                  #ファイル名
