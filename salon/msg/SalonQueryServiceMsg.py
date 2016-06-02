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

    
class SalonSrhItemMsg(messages.Message):
    u"""サロン 検索結果"""
    oneHourPoint= messages.IntegerField(1)                #一時間利用ポイント
    oneDayPoint= messages.IntegerField(2)                 #一日利用ポイント
    compEval= messages.FloatField(3)                      #総合評価
    stationName= messages.StringField(4)                    #最寄り駅
    workingTime= messages.IntegerField(5)                     #駅徒歩
    name= messages.StringField(6)                         #店舗名
    mainImgFileName= messages.StringField(7)              #メイン画像ファイル名

class SalonSearchByKeywordMsg(messages.Message):
    u"""サロンアカウント新規登録結果メッセージ"""
    keyword = messages.StringField(1)                    #キーワード
    pos = messages.IntegerField(2)                       #取得ポジション(1〜
    limit = messages.IntegerField(3)                     #取得数
    orderCol = messages.IntegerField(4)                 #出力潤

class SalonSearchByKeywordResMsg(messages.Message):
    u"""サロンアカウント新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    count =  messages.IntegerField(2)                   #検索対象数
    salons = messages.MessageField(SalonSrhItemMsg, 3, repeated=True)   #検索結果
    



