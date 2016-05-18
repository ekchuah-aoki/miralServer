# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.AccountKind import AccountKind

class SalonReviewKind(BaseKind):
    u"""サロンレビュー情報"""
    accountId = ndb.StringProperty()                                  #サロンアカウントKeyId
    rvBeautiKey = ndb.KeyProperty(kind=AccountKind)                   #レビュー美容師Key
    evaluation = ndb.FloatProperty()                                  #評価
    review = ndb.TextProperty()                                       #レビューコメント
