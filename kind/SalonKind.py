# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class SalonKind(BaseKind):
    u"""サロン情報"""
    accountKey = ndb.KeyProperty(index=True,"kind=AccountKind")       #アカウントKey
    name = ndb.StringProperty()                                       #店舗名
    nameKana = ndb.StringProperty()                                   #店舗名カナ
    prefecturesCd = ndb.IntegerProperty()                             #都道府県
    streetAdd1 = ndb.StringProperty()                                 #住所１
    streetAdd2 = ndb.StringProperty()                                 #住所２
    stationCd = ndb.IntegerProperty()                                 #最寄り駅
    workingTime = ndb.IntegerProperty()                               #駅徒歩
    geoCd = ndb.GeoPtProperty()                                       #緯度：軽度
    compEval = ndb.FloatProperty()                                    #総合評価
    oneHourPoint = ndb.IntegerProperty()                              #１時間利用ポイント
    oneDayPoint = ndb.IntegerProperty()                               #１日利用ポイント
    conditions = ndb.TextProperty()                                   #利用条件
    cancelPer = ndb.FloatProperty()                                   #キャンセル割合
    holiday = ndb.StringProperty()                                    #定休日
    hpUrl = ndb.StringProperty()                                      #HP URL
    email = ndb.StringProperty()                                      #E mailアドレス
    parkingCd = ndb.IntegerProperty()                                 #駐車場区分
    parkingRem = ndb.StringProperty()                                 #駐車場備考
    remarks = ndb.TextProperty()                                      #備考
    ownerPhotoUrl = ndb.StringProperty()                              #オーナー画像URL
    owrnerComme = ndb.TextProperty()                                  #オーナーからの一言
    openTime = ndb.TimeProperty()                                     #営業時間開始
    closeTime = ndb.TimeProperty()                                    #営業時間終了
    srhCondPref = ndb.IntegerProperty(repeated=True)                  #検索対象都道府県
    srhCondIowestRat = ndb.FloatProperty()                            #検索対象最低総合評価
    salonGalleryKeyList = ndb.KeyProperty(repeated=True,"kind=SalonGalleryKind") #プロフィール画像
    mirrorCnt = ndb.IntegerProperty()                                 #利用可能席数
