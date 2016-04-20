# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class BeauticianKind(BaseKind):
    u"""美容師情報"""
    accountKey = ndb.KeyProperty("kind=AccountKind")                  #アカウントKey
    nickName = ndb.StringProperty()                                   #ニックネーム
    compEval = ndb.FloatProperty()                                    #総合評価
    careerYears = ndb.IntegerProperty()                               #経歴年数
    pr = ndb.IntegerProperty()                                        #自己PR
    licenseFlg = ndb.TextProperty()                                   #美容師免許承認済みフラグ
    srhCondPref = ndb.IntegerProperty(repeated=True)                  #検索対象都道府県
    srhCondIowestRat = ndb.FloatProperty()                            #検索対象最低総合評価
    BeauticianMyGalleryKeyList = ndb.KeyProperty(repeated=True,"kind=BeauticianMyGalleryKind")     #プロフィール画像
    BeauticianWorkGalleryKeyList = ndb.KeyProperty(repeated=True,"kind=BeauticianWorkGalleryKind") #実績画像
