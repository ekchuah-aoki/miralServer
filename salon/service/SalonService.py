# coding: UTF-8
from protorpc import messages
from google.appengine.ext import ndb

from common.msg.ApiResponceMsg import ApiResponceMsg
from kind.AccountKind import AccountKind
from code.LOGIN_TYPE import LOGIN_TYPE
from code.OK_NG import OK_NG
from code.ACCOUNT_TYPE import ACCOUNT_TYPE
from common.MiralLogger import MiralLogger
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralMsgTbl import MiralMsgTbl
from kind.SalonKind import SalonKind
from common.DateUtil import DateUtil
from common.service.AccountService import AccountService
from common.service.AccountService import AccountMsg

from salon.msg.SalonServiceMsg import SalonAccountAddResMsg 
from salon.msg.SalonServiceMsg import SalonAccountModifyResMsg 
from salon.msg.SalonServiceMsg import SalonAccountEditMsg 
from salon.msg.SalonServiceMsg import SalonGetAccount4EditResMsg 

from common.service.TrainMastrService import TrainRouteService

class SalonService():
    u"""サロンサービス"""
    
    def __covMsg2Knd(self, k_, m_, stationKey_):
        logger = MiralLogger()
        
        
        k_.name = m_.name                                                   #店舗名
        k_.nameKana = m_.nameKana                                           #店舗名カナ
        k_.prefecturesCd = m_.prefecturesCd2                                #都道府県
        k_.streetAdd1 = m_.streetAdd1                                       #住所１
        k_.streetAdd2 = m_.streetAdd2                                       #住所２
        #k_.stationKey = trainService.getStationKeyByCode(m_.stationCd)     #最寄り駅
        k_.stationKey = stationKey_           #最寄り駅
        k_.workingTime = m_.workingTime                                     #駅徒歩
        
        if m_.lat:
            k_.geoCd = ndb.GeoPt(m_.lat + "," + m_.lng)                         #GEOコード      
        
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
    
    @ndb.transactional(xg=True)
    def __addAcount(self, reqMsg_, stationKey_):
        
        #サロン情報登録
        salonKnd = SalonKind()
        self.__covMsg2Knd(salonKnd,reqMsg_.salon, stationKey_)
        salonKnd.put()
        
        #アカウント情報登録
        accountKnd = AccountKind()
        accountKnd.email = reqMsg_.salon.email                            #EMailアドレス
        accountKnd.acType = ACCOUNT_TYPE.salon.getCode()                          #アカウント種別
         
        accountKnd.lastName = reqMsg_.salon.lastName                      #氏名(苗字)
        accountKnd.firstName = reqMsg_.salon.firstName                    #氏名(名前)
        accountKnd.lastNameKana = reqMsg_.salon.lastNameKana              #氏名カナ(苗字)
        accountKnd.firstNameKana = reqMsg_.salon.firstNameKana            #氏名カナ(名前)
        accountKnd.prefecturesCd = reqMsg_.salon.prefecturesCd1            #都道府県
        accountKnd.tell = reqMsg_.salon.tell                              #電話番号
        accountKnd.passWord = reqMsg_.salon.passWord                      #パスワード
        
        accountKnd.temporary = False                     #仮登録フラグ
        
        accountKnd.salonKey = salonKnd.key
        
        accountKnd.put()
        
        return accountKnd
    
    def add(self, salonAccountAddMsg_):
        u"""サロンアカウント新規登録"""
        
        logger = MiralLogger()
        
        accountService = AccountService()
        resMsg = SalonAccountAddResMsg()
        
        #アカウント（Email)の存在チェック
        if accountService.isEmailExists(salonAccountAddMsg_.salon.email):
            resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
            return resMsg
        
        #TODO:今はテスト的に固定
        trainService = TrainRouteService()
        stationKey = trainService.getStationKeyByCode(1130314)        
        accountKnd = self.__addAcount(salonAccountAddMsg_, stationKey)
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        logger.debug("--------- SalonService add!"+str(accountKnd.salonKey.id()))
        resMsg.accountId = str(accountKnd.key.id())
        resMsg.kindId = str(accountKnd.salonKey.id())

        return resMsg    

    @ndb.transactional(xg=True)
    def __modiyAccount(self, reqMsg_, stationKey_):
        #アカウント情報
        accountKey = ndb.Key(AccountKind, long(reqMsg_.accountId))
        accountKnd = accountKey.get()

        accountKnd.email = reqMsg_.salon.email                            #EMailアドレス
         
        accountKnd.lastName = reqMsg_.salon.lastName                      #氏名(苗字)
        accountKnd.firstName = reqMsg_.salon.firstName                    #氏名(名前)
        accountKnd.lastNameKana = reqMsg_.salon.lastNameKana              #氏名カナ(苗字)
        accountKnd.firstNameKana = reqMsg_.salon.firstNameKana            #氏名カナ(名前)
        accountKnd.prefecturesCd = reqMsg_.salon.prefecturesCd2           #都道府県
        accountKnd.tell = reqMsg_.salon.tell                              #電話番号
        
        if reqMsg_.beauti.passWord:
            accountKnd.passWord = reqMsg_.salon.passWord

        accountKnd.put()

        salonKnd = accountKnd.salonKey.get()
        

        self.__covMsg2Knd(salonKnd,reqMsg_.salon, stationKey_)
        salonKnd.put()

        

    def modify(self, salonAccountModifyMsg_):
        u"""サロンアカウント情報変更"""
        
        logger = MiralLogger()
        
        resMsg = SalonAccountModifyResMsg()

        trainService = TrainRouteService()
        stationKey = trainService.getStationKeyByCode(1130314)        
        
        self.__modiyAccount(salonAccountModifyMsg_,stationKey)
        
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

    def getAccount4Edit(self, reqMsg_):
        logger = MiralLogger()
        logger.debug("--------- SalonService getAccount4Edit start!")        
        
        salonMsg = SalonAccountEditMsg()

        accountKey = ndb.Key(AccountKind, long(reqMsg_.accountId))
        accountKnd = accountKey.get()

        #アカウント共通情報
        salonMsg.email = accountKnd.email                            #EMailアドレス
        salonMsg.lastName = accountKnd.lastName                      #氏名(苗字)
        salonMsg.firstName = accountKnd.firstName                    #氏名(名前)
        salonMsg.lastNameKana = accountKnd.lastNameKana              #氏名カナ(苗字)
        salonMsg.firstNameKana = accountKnd.firstNameKana            #氏名カナ(名前)
        salonMsg.prefecturesCd1 = accountKnd.prefecturesCd           #都道府県
        salonMsg.tell = accountKnd.tell                              #電話番号
        
        salonKnd = accountKnd.salonKey.get()

        #アカウントサロン情報
        salonMsg.name = salonKnd.name                                #店舗名カナ
        salonMsg.nameKana = salonKnd.nameKana                        #店舗名カナ
        salonMsg.prefecturesCd2 = salonKnd.prefecturesCd             #店舗所在地都道府県
        salonMsg.streetAdd1 =salonKnd.streetAdd1                     #店舗所在地住所１
        salonMsg.streetAdd2 = salonKnd.streetAdd2                    #店舗所在地住所２
        
        if salonKnd.geoCd: 
            salonMsg.lat = str(salonKnd.geoCd.lat)                       #店舗所在地緯度
            salonMsg.lng = str(salonKnd.geoCd.lon)                       #店舗所在地軽度
            
        salonMsg.stationCd = salonKnd.stationCd                      #最寄り駅
        salonMsg.workingTime = salonKnd.workingTime                  #駅徒歩
        salonMsg.oneHourPoint = salonKnd.oneHourPoint                #１時間利用ポイント
        salonMsg.oneDayPoint = salonKnd.oneDayPoint                  #１日利用ポイント
        salonMsg.conditions = salonKnd.conditions                    #利用条件
        salonMsg.cancelPer = salonKnd.cancelPer                      #キャンセル割合
        salonMsg.holiday = salonKnd.holiday                          #定休日
        salonMsg.hpUrl = salonKnd.hpUrl                              #HP URL
        
        openTime = DateUtil.splitStrTime(salonKnd.openTime)
        salonMsg.openTime = openTime["hour"]+openTime["minute"]            #営業時間開始

        closeTime = DateUtil.splitStrTime(salonKnd.closeTime)
        salonMsg.closeTime = closeTime["hour"]+closeTime["minute"]         #営業時間終了
        salonMsg.mirrorCnt = salonKnd.mirrorCnt                      #利用可能席数
        
        resMsg = SalonGetAccount4EditResMsg()
        resMsg.salon = salonMsg
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
        
        return resMsg
    
