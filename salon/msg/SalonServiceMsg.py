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

class SalonAccountEditMsg(messages.Message):
    u"""サロン情報（アカウント編集用）"""
    
    
    email = messages.StringField(1)                         #EMailアドレス
    lastName = messages.StringField(2)                      #氏名(苗字)
    firstName = messages.StringField(3)                     #氏名(名前)
    lastNameKana = messages.StringField(4)                  #氏名カナ(苗字)
    firstNameKana = messages.StringField(5)                 #氏名カナ(名前)
    prefecturesCd1 = messages.IntegerField(6)                #都道府県コード
    tell = messages.StringField(7)                          #電話番号
    passWord = messages.StringField(8)                      #パスワード
    
    name = messages.StringField(9)                                       #店舗名
    nameKana = messages.StringField(10)                                   #店舗名カナ
    prefecturesCd2 = messages.IntegerField(11)                             #店舗所在地都道府県
    streetAdd1 = messages.StringField(12)                                 #店舗所在地住所１
    streetAdd2 = messages.StringField(13)                                 #店舗所在地住所２
    lat = messages.StringField(14)                                        #店舗所在地緯度
    lng = messages.StringField(15)                                        #店舗所在地軽度
    stationCd = messages.IntegerField(16)                                 #最寄り駅
    workingTime = messages.IntegerField(17)                               #駅徒歩
    oneHourPoint = messages.IntegerField(18)                              #１時間利用ポイント
    oneDayPoint = messages.IntegerField(19)                               #１日利用ポイント
    conditions = messages.StringField(20)                                 #利用条件
    cancelPer = messages.FloatField(21)                                   #キャンセル割合
    holiday = messages.StringField(22,repeated=True)                      #定休日
    hpUrl = messages.StringField(23)                                      #HP URL
    openTime = messages.StringField(24)                                   #営業時間開始
    closeTime = messages.StringField(25)                                  #営業時間終了
    mirrorCnt = messages.IntegerField(26)                                 #利用可能席数

class SalonAccountAddMsg(messages.Message):
    u"""サロンアカウント新規登録依頼メッセージ"""
    salon = messages.MessageField(SalonAccountEditMsg, 1)          #サロン情報

class SalonAccountAddResMsg(messages.Message):
    u"""サロンアカウント新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    accountId = messages.StringField(2)                 #アカウントID
    kindId = messages.StringField(3)                    #KindID


class SalonGetAccount4EditMsg(messages.Message):
    accountId = messages.StringField(1)                         #アカウントId

class SalonGetAccount4EditResMsg(messages.Message):
    res = messages.MessageField(ApiResponceMsg, 1)                  #結果
    salon = messages.MessageField(SalonAccountEditMsg, 2)     #アカウント情報


class SalonAccountModifyMsg(messages.Message):
    u"""サロンアカウント修正依頼メッセージ"""
    accountId = messages.StringField(1)                 #アカウントID
    salon = messages.MessageField(SalonAccountEditMsg, 2)          #サロン情報

class SalonAccountModifyResMsg(messages.Message):
    u"""サロンアカウント修正結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果

class SalonProfileBasicModifyMsg(messages.Message):
    u"""サロンプロファイル修正依頼メッセージ"""
    salonId = messages.MessageField(AccountMsg, 1)       #アカウント情報
    salon = messages.MessageField(SalonAccountEditMsg, 2)          #サロン情報

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



