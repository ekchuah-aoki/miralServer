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
    
    accountId = messages.StringField                                    #アカウントId
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

class SalonOwnerImgAddMsg(messages.Message):
    u"""オーナ画像登録依頼メッセージ"""
    accountId = messages.StringField(1)                 #アカウントID
    imgbase64data = messages.StringField(2)              #イメージデータ

class SalonOwnerImgAddResMsg(messages.Message):
    u"""オーナー画像登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果


class SalonService():
    u"""サロンサービス"""
    
    @ndb.transactional(xg=True)    
    def _add(self, accountSalonAddMsg_):
       
        #アカウント情報登録
        accountService = AccountService()
        accountKey = accountService.add(accountSalonAddMsg_.account)
        
        #サロン情報登録
        salonMsg = accountSalonAddMsg_.salon
        salonKnd = SalonKind()

        salonKnd.accountKey = accountKey

        salonKnd.name = salonMsg.name                                                   #店舗名
        salonKnd.nameKana = salonMsg.nameKana                                           #店舗名カナ
        salonKnd.prefecturesCd = salonMsg.prefecturesCd                                 #都道府県
        salonKnd.streetAdd1 = salonMsg.streetAdd1                                       #住所１
        salonKnd.streetAdd2 = salonMsg.streetAdd2                                       #住所２
        salonKnd.stationCd = salonMsg.stationCd                                         #最寄り駅
        salonKnd.workingTime = salonMsg.messages.IntegerField()                         #駅徒歩
        
        salonKnd.geoCd = ndb.GeoPt(salonMsg.lat + "," + salonMsg.lon)                   #GEOコード      
        
        salonKnd.compEval = salonMsg.compEval                                           #総合評価
        salonKnd.oneHourPoint = salonMsg.oneHourPoint                                   #１時間利用ポイント
        salonKnd.oneDayPoint = salonMsg.oneDayPoint                                     #１日利用ポイント
         
        salonKnd.conditions = salonMsg.conditions                                       #利用条件    

        salonKnd.cancelPer = salonMsg.cancelPer                                         #キャンセル割合            
        salonKnd.holiday = salonMsg.holiday                                             #定休日
        salonKnd.hpUrl = salonMsg.hpUrl                                                 #HP URL

        salonKnd.email = salonMsg.email                                                 #E mailアドレス

        salonKnd.parkingCd = salonMsg.parkingCd                                         #駐車場区分
        salonKnd.parkingRem = salonMsg.parkingRem                                       #駐車場備考
        
        salonKnd.remarks = salonMsg.remarks                                             #備考
        salonKnd.openTime = DateUtil.getTimeByStr(salonMsg.openTime+"00")               #営業時間開始
        salonKnd.closeTime = DateUtil.getTimeByStr(salonMsg.closeTime+"00")             #営業時間開始
        
        salonKnd.put();
        
        return salonKnd.key;
    
    def add(self, salonAccountAddMsg_):
        
        logger = MiralLogger()
        
        accountService = AccountService()
        resMsg = SalonAccountAddResMsg()
        
        #アカウント（Email)の存在チェック
        if accountService.isEmailExists(salonAccountAddMsg_.account.email):
            resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
            return resMsg
        
        
        salonKey = self._add(salonAccountAddMsg_)
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        logger.debug("--------- SalonService add!"+str(salonKey.id()))
        resMsg.kindId = str(salonKey.id())

        return resMsg    
            