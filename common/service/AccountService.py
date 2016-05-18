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

    
    def add(self, accountMsg_, kindKey_):
        
        logger = MiralLogger()
        
        accountKnd = AccountKind()
        
        self.__covMsg2Knd(accountMsg_, accountKnd, True) 
        
        if accountMsg_.acType == ACCOUNT_TYPE.beauti.getCode():
            accountKnd.beautiKey = kindKey_
        else:
            accountKnd.salonKey = kindKey_
        
        accountKnd.put()
        
        logger.debug("AccountService add ok!")
        return accountKnd.key
        
    def modify(self, accountMsg_):
        
        logger = MiralLogger()
        
        accountKey = ndb.Key('AccountKind', accountMsg_.accountid)
        accountKnd = accountKey.get()
        
        self.__covMsg2Knd(accountMsg_, accountKnd, False) 
        
        accountKnd.put()
        
        logger.debug("AccountService modify ok!")
        return
    
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
        
    def __covMsg2Knd(self, m_, k_, addMode):
        
        if addMode:
            k_.email = m_.email                            #EMailアドレス
            k_.acType = m_.acType                          #アカウント種別
            k_.facebookId = m_.facebookId                  #FacebookID
            k_.facebookToke = m_.facebookToke              #FacebookToken
            k_.twitterId = m_.twitterId                    #TwitterId   
            k_.twitterToken = m_.twitterToken              #TwitterToken  
            k_.googleplusId = m_.googleplusId              #googleId   
            k_.googleplusToken = m_.googleplusToken        #googleToken      
            k_.instagramId = m_.instagramId                #instagramId   
            k_.instagramToken = m_.instagramToken          #instagramToken
            
         
        k_.lastName = m_.lastName                      #氏名(苗字)
        k_.firstName = m_.firstName                    #氏名(名前)
        k_.lastNameKana = m_.lastNameKana              #氏名カナ(苗字)
        k_.firstNameKana = m_.firstNameKana            #氏名カナ(名前)
        k_.prefecturesCd = m_.prefecturesCd            #都道府県
        k_.tell = m_.tell                              #電話番号
        k_.passWord = m_.passWord                      #パスワード
        
        k_.temporary = m_.temporary                     #仮登録フラグ
            