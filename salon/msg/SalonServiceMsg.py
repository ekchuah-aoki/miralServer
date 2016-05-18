# coding: UTF-8
from protorpc import messages
from google.appengine.ext import ndb

from common.msg.ApiResponceMsg import ApiResponceMsg
from kind.AccountKind import AccountKind
from code.LOGIN_TYPE import LOGIN_TYPE
from code.OK_NG import OK_NG
from code.UMU_FLG import UMU_FLG
from common.MiralLogger import MiralLogger
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralMsgTbl import MiralMsgTbl
from kind.SalonKind import SalonKind
from common.DateUtil import DateUtil
from common.service.AccountService import AccountService
from common.service.AccountService import AccountMsg

class SalonMsg(messages.Message):
    u"""サロン情報"""
    name = messages.StringField()                                       #店舗名
    nameKana = messages.StringField()                                   #店舗名カナ
    prefecturesCd = messages.IntegerField()                             #都道府県
    streetAdd1 = messages.StringField()                                 #住所１
    streetAdd2 = messages.StringField()                                 #住所２
    stationCd = messages.IntegerField()                                 #最寄り駅
    workingTime = messages.IntegerField()                               #駅徒歩
    lat = messages.StringField()                                        #緯度
    lon = messages.StringField()                                        #経度
    compEval = messages.FloatField()                                    #総合評価
    oneHourPoint = messages.IntegerField()                              #１時間利用ポイント
    oneDayPoint = messages.IntegerField()                               #１日利用ポイント
    conditions = messages.StringField()                                 #利用条件
    cancelPer = messages.FloatField()                                   #キャンセル割合
    holiday = messages.StringField()                                    #定休日
    hpUrl = messages.StringField()                                      #HP URL
    email = messages.StringField()                                      #E mailアドレス
    parkingCd = messages.IntegerField()                                 #駐車場区分
    parkingRem = messages.StringField()                                 #駐車場備考
    remarks = messages.StringField()                                    #備考
    ownerThImage = messages.StringField()                               #オーナーサムネイルファイル名
    owrnerComme = messages.StringField()                                #オーナーからの一言
    openTime = messages.StringField()                                   #営業時間開始
    closeTime = messages.StringField()                                  #営業時間終了
    srhCondPref = messages.IntegerField(repeated=True)                  #美容師検索対象都道府県
    srhCondIowestRat = messages.FloatField()                            #美容師検索対象最低総合評価
    salonGalleryThImgList = messages.StringField(repeated=True)         #プロフィール画像ファイル名
    mirrorCnt = messages.IntegerField()                                 #利用可能席数

class SalonAccountAddMsg(messages.Message):
    u"""サロンアカウント新規登録依頼メッセージ"""
    account = messages.MessageField(AccountMsg, 1)      #アカウント情報
    salon = messages.MessageField(SalonMsg, 2)          #サロン情報

class SalonAccountAddResMsg(messages.Message):
    u"""サロンアカウント新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    kindId = messages.StringField(2)                    #KindID


class SalonAccountModifyMsg(messages.Message):
    u"""サロンアカウント修正依頼メッセージ"""
    account = messages.MessageField(AccountMsg, 1)      #アカウント情報
    salon = messages.MessageField(SalonMsg, 2)          #サロン情報

class SalonAccountModifyResMsg(messages.Message):
    u"""サロンアカウント修正結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果

class SalonProfileBasicModifyMsg(messages.Message):
    u"""サロンプロファイル修正依頼メッセージ"""
    salonId = messages.StringField(AccountMsg, 1)       #アカウント情報
    salon = messages.MessageField(SalonMsg, 2)          #サロン情報

class SalonProfileBasicModifyResMsg(messages.Message):
    u"""サロンプロファイル修正結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果

class SalonOwnerImgSetMsg(messages.Message):
    u"""オーナ画像登録依頼メッセージ"""
    accountId = messages.StringField(1)                 #アカウントID
    imgbase64data = messages.StringField(2)             #イメージデータ

class SalonOwnerImgSetResMsg(messages.Message):
    u"""オーナー画像登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果



