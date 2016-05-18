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

from salon.msg.SalonServiceMsg import SalonAccountAddResMsg 
from salon.msg.SalonServiceMsg import SalonAccountModifyResMsg 
class SalonService():
    u"""サロンサービス"""
    
    @ndb.transactional(xg=True)    
       
     
    def __covMsg2Knd(self, k_, m_):
        k_.name = m_.name                                                   #店舗名
        k_.nameKana = m_.nameKana                                           #店舗名カナ
        k_.prefecturesCd = m_.prefecturesCd                                 #都道府県
        k_.streetAdd1 = m_.streetAdd1                                       #住所１
        k_.streetAdd2 = m_.streetAdd2                                       #住所２
        k_.stationCd = m_.stationCd                                         #最寄り駅
        k_.workingTime = m_.messages.IntegerField()                         #駅徒歩
        
        k_.geoCd = ndb.GeoPt(m_.lat + "," + m_.lon)                         #GEOコード      
        
        k_.compEval = m_.compEval                                           #総合評価
        k_.oneHourPoint = m_.oneHourPoint                                   #１時間利用ポイント
        k_.oneDayPoint = m_.oneDayPoint                                     #１日利用ポイント
         
        k_.conditions = m_.conditions                                       #利用条件    

        k_.cancelPer = m_.cancelPer                                         #キャンセル割合            
        k_.holiday = m_.holiday                                             #定休日
        k_.hpUrl = m_.hpUrl                                                 #HP URL

        k_.openTime = DateUtil.getTimeByStr(m_.openTime+"00")               #営業時間開始
        k_.closeTime = DateUtil.getTimeByStr(m_.closeTime+"00")             #営業時間開始
        
    def __covProfileBasicMsg2Knd(self, k_, m_):
        k_.remarks = m_.remarks                                             #備考
        k_.owrnerComme = m_.owrnerComme                                     #オーナーからの一言
    
    def add(self, salonAccountAddMsg_):
        u"""サロンアカウント新規登録"""
        
        logger = MiralLogger()
        
        accountService = AccountService()
        resMsg = SalonAccountAddResMsg()
        
        #アカウント（Email)の存在チェック
        if accountService.isEmailExists(salonAccountAddMsg_.account.email):
            resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
            return resMsg
        
        
        #サロン情報登録
        salonKnd = SalonKind()

        self.__covMsg2Knd(salonKnd,salonAccountAddMsg_.salon)
        salonKnd.put()
        
        #アカウント情報登録
        accountService = AccountService()
        accountService.add(salonAccountAddMsg_.account, salonKnd.key)
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        logger.debug("--------- SalonService add!"+str(salonKnd.key.id()))
        resMsg.kindId = str(salonKnd.key.id())

        return resMsg    

    def modify(self, salonAccountModifyMsg_):
        u"""サロンアカウント情報変更"""
        
        logger = MiralLogger()
        
        accountService = AccountService()
        resMsg = SalonAccountModifyResMsg()
        
        salonKey = self._add(salonAccountModifyMsg_)
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        logger.debug("--------- SalonService modify!")

        return resMsg    

    def modifyProfileBasic(self, salonProfileBasicModifyMsg_):
        u"""サロンプロフィール基本情報変更（オーナー画像以外）"""
        
        logger = MiralLogger()
        
        salonKey = ndb.Key(SalonKind, salonProfileBasicModifyMsg_.salonid)
        
        salonKind = salonKey.get()
        
        self.__covProfileBasicMsg2Knd(salonKind, salonProfileBasicModifyMsg_.salonid)

        salonKind.put()

