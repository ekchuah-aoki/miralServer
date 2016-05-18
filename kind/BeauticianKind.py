# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.BeauticianLicenseKind import BeauticianLicenseKind
from kind.BeauticianMyGalleryKind import BeauticianMyGalleryKind
from kind.BeauticianWorkGalleryKind import BeauticianWorkGalleryKind


class BeauticianKind(BaseKind):
    u"""美容師情報"""
    nickName = ndb.StringProperty()                                   #ニックネーム
    compEval = ndb.FloatProperty()                                    #総合評価
    pr = ndb.IntegerProperty()                                        #自己PR
    totalPoint = ndb.IntegerProperty(default=0)                       #所有合計ポイント
    gender = ndb.IntegerProperty()                                    #性別
    birthday = ndb.DateProperty()                                     #生年月日
    licenseFlg = ndb.TextProperty()                                   #美容師免許承認済みフラグ
    srhCondPref = ndb.IntegerProperty(repeated=True)                  #検索対象都道府県
    srhCondIowestRat = ndb.FloatProperty()                            #検索対象最低総合評価

    licenseKey = ndb.KeyProperty(kind=BeauticianLicenseKind)
    myGalleryKey = ndb.KeyProperty(repeated=True, kind=BeauticianMyGalleryKind)  
    workGalleryKey = ndb.KeyProperty(repeated=True, kind=BeauticianWorkGalleryKind)  
