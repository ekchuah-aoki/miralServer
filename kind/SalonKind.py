# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.ImageKind import ImageKind
from kind.SalonGalleryKind import SalonGalleryKind
from kind.SalonFacilityKind import SalonFacilityKind
from kind.SalonExpendableKind import SalonExpendableKind
from kind.master.MstStationKind import MstStationKind

class SalonKind(BaseKind):
    u"""サロン情報"""
    name = ndb.StringProperty()                                       #店舗名
    nameKana = ndb.StringProperty()                                   #店舗名カナ
    prefecturesCd = ndb.IntegerProperty()                             #都道府県
    streetAdd1 = ndb.StringProperty()                                 #住所１
    streetAdd2 = ndb.StringProperty()                                 #住所２
    stationKey = ndb.KeyProperty(kind=MstStationKind)                                 #最寄り駅
    workingTime = ndb.IntegerProperty()                               #駅徒歩
    geoCd = ndb.GeoPtProperty()                                       #緯度：軽度
    compEval = ndb.FloatProperty(default=0)                           #総合評価
    oneHourPoint = ndb.IntegerProperty(default=0)                     #１時間利用ポイント
    oneDayPoint = ndb.IntegerProperty(default=0)                      #１日利用ポイント
    conditions = ndb.TextProperty()                                   #利用条件
    cancelPer = ndb.FloatProperty()                                   #キャンセル割合
    holiday = ndb.StringProperty(repeated=True)                                    #定休日
    hpUrl = ndb.StringProperty()                                      #HP URL
    email = ndb.StringProperty()                                      #連絡用Emailアドレス
    parkingCd = ndb.IntegerProperty()                                 #駐車場利用区分
    parkingRem = ndb.StringProperty()                                 #駐車場備考
    remarks = ndb.TextProperty()                                      #備考
    ownerThImageKey = ndb.KeyProperty(kind=ImageKind)                 #オーナーサムネイル画像Key
    owrnerComme = ndb.TextProperty()                                  #オーナーからの一言
    openTime = ndb.TimeProperty()                                     #営業時間開始
    closeTime = ndb.TimeProperty()                                    #営業時間終了
    srhCondPref = ndb.IntegerProperty(repeated=True)                  #美容師検索対象都道府県
    srhCondIowestRat = ndb.FloatProperty()                            #美容師検索対象最低総合評価
    mirrorCnt = ndb.IntegerProperty()                                 #利用可能席数

    mainImageKey = ndb.KeyProperty(kind=ImageKind)  
    galleryKey = ndb.KeyProperty(kind=SalonGalleryKind)  
    facilityKey = ndb.KeyProperty(kind=SalonFacilityKind)  
    expendableKey = ndb.KeyProperty(kind=SalonExpendableKind)  

    