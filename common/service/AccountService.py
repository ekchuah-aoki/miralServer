# coding: UTF-8
from protorpc import messages
from datetime import date
from google.appengine.ext import ndb

from kind.AccountKind import AccountKind
from code.LOGIN_TYPE import LOGIN_TYPE
from code.OK_NG import OK_NG
from code.UMU_FLG import UMU_FLG
from code.ACCOUNT_TYPE import ACCOUNT_TYPE
from common.MiralLogger import MiralLogger
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralMsgTbl import MiralMsgTbl
from kind.BeauticianKind import BeauticianKind

from common.msg.AccountServiceMsg import AccountMsg
from common.msg.AccountServiceMsg import AccountGetResMsg
from common.msg.AccountServiceMsg import AccountGetLoginResMsg

from common.CommUtil import CommUtil

class AccountService():
    u"""アカウントサービス"""

         
    def getKind(self, id_):
        accountKey = ndb.Key(AccountKind, id_)
        return accountKey.get()
        
        
    def get(self, loginType_, id_):
        u"""アカウント情報取得"""
        
        logger = MiralLogger()

        logger.debug('get loginType:' + str(loginType_) + ' id:' + id_)
        
        if LOGIN_TYPE.facebook.getCode()==loginType_:
            acq = AccountKind.query(AccountKind.facebookId == id_)
            
            logger.debug('check facebook')
            
        elif LOGIN_TYPE.twitter.equalCd(loginType_):     
            acq = AccountKind.query(AccountKind.twitterId == id_)
        elif LOGIN_TYPE.instagram.equalCd(loginType_):     
            acq = AccountKind.query(AccountKind.instagramId == id_)
        elif LOGIN_TYPE.googleplus.equalCd(loginType_):     
            acq = AccountKind.query(AccountKind.googleplusId == id_)
        else:
            acq = AccountKind.query(AccountKind.email == id_)
            logger.debug('check email')
            
        accountKnd = acq.get()


        resMsg = AccountGetResMsg()
        
        if not accountKnd:
            logger.debug("loginType:"+str(loginType_) +" id:"+id_+u" は存在しません")
            resMsg.res = ApiResponceMsg(rstCode=UMU_FLG.nasi.getCode())
            return resMsg
        
        
        accountMsg =  AccountMsg()
        self.covKnd2Msg(accountKnd, accountMsg)

        
        resMsg.res = ApiResponceMsg(rstCode=UMU_FLG.ari.getCode())
        resMsg.account = accountMsg 
        return resMsg
    

    def getLogin(self, loginType_, id_):
        u"""アカウント情報取得"""
        
        logger = MiralLogger()

        logger.debug('get loginType:' + str(loginType_) + ' id:' + id_)

        resMsg = AccountGetLoginResMsg()
        
        if LOGIN_TYPE.facebook.getCode()==loginType_:
            acq = AccountKind.query(AccountKind.facebookId == id_)
            
            logger.debug('check facebook')
            
        elif LOGIN_TYPE.twitter.equalCd(loginType_):     
            acq = AccountKind.query(AccountKind.twitterId == id_)
        elif LOGIN_TYPE.instagram.equalCd(loginType_):     
            acq = AccountKind.query(AccountKind.instagramId == id_)
        elif LOGIN_TYPE.googleplus.equalCd(loginType_):     
            acq = AccountKind.query(AccountKind.googleplusId == id_)
        else:
            acq = AccountKind.query(AccountKind.email == id_)
            logger.debug('check email')
            
        accountKnd = acq.get()


        
        if not accountKnd:
            logger.debug("loginType:"+str(loginType_) +" id:"+id_+u" は存在しません")
            resMsg.res = ApiResponceMsg(rstCode=UMU_FLG.nasi.getCode())
            return resMsg
        
        
        resMsg.email = accountKnd.email                            #EMailアドレス
        resMsg.acType = accountKnd.acType                          #アカウント種別
        resMsg.lastName = accountKnd.lastName                      #氏名(苗字)
        resMsg.firstName = accountKnd.firstName                    #氏名(名前)
        resMsg.temporary = accountKnd.temporary                    #仮登録フラグ 
        resMsg.accountId = str(accountKnd.key.id()) 
        
        if  accountKnd.acType == ACCOUNT_TYPE.beauti.getCode():
            resMsg.kindId = str(accountKnd.beautiKey.id())
        else:
            resMsg.kindId = str(accountKnd.salonKey.id())              

        
        resMsg.res = ApiResponceMsg(rstCode=UMU_FLG.ari.getCode())
        return resMsg
    
    
    
    def isEmailExists(self, email_, id_=""):
        
        acq = AccountKind.query(AccountKind.email == email_)
        existAccountKey = acq.get(keys_only=True)
        if existAccountKey:
            
            if id_ != "" and existAccountKey.id() != id_:
                return False
            
            return True
        
        return False
    
    def getBeautiKeyByAccountId(self, accountId_):
        
        accountKey = ndb.Key(AccountKind, accountId_)
        
        accountKind = accountKey.get()
        
        return accountKind.beautiKey
    
        
    def getSalonKeyByAccountId(self, accountId_):
        accountKey = ndb.Key(AccountKind, accountId_)
        
        accountKind = accountKey.get()
        
        return accountKind.salonKey

    
    
    def covKnd2Msg(self, k_, m_):
        m_.email = k_.email                            #EMailアドレス
        m_.acType = k_.acType                          #アカウント種別
        m_.lastName = k_.lastName                      #氏名(苗字)
        m_.firstName = k_.firstName                    #氏名(名前)
        m_.lastNameKana = k_.lastNameKana              #氏名カナ(苗字)
        m_.firstNameKana = k_.firstNameKana            #氏名カナ(名前)
        m_.prefecturesCd = k_.prefecturesCd            #都道府県
        m_.tell = k_.tell                              #電話番号
        m_.passWord = k_.passWord                      #パスワード
        m_.facebookId = k_.facebookId                  #FacebookID
        m_.facebookToke = k_.facebookToke              #FacebookToken
        m_.twitterId = k_.twitterId                    #TwitterId   
        m_.twitterToken = k_.twitterToken              #TwitterToken  
        m_.googleplusId = k_.googleplusId            #googleId   
        m_.googleplusToken = k_.googleplusToken        #googleToken      
        m_.instagramId = k_.instagramId                #instagramId   
        m_.instagramToken = k_.instagramToken          #instagramToken 

        m_.temporary = k_.temporary                    #仮登録フラグ 
        
        m_.accountId = str(k_.key.id()) 
        
        if  k_.acType == ACCOUNT_TYPE.beauti.getCode():
            m_.kindId = str(k_.beautiKey.id())
        else:
            m_.kindId = str(k_.salonKey.id())              
