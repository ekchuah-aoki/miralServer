# coding: UTF-8
from protorpc import messages
from datetime import date

from kind.AccountKind import AccountKind
from code.LOGIN_TYPE import LOGIN_TYPE
from code.OK_NG import OK_NG
from code.UMU_FLG import UMU_FLG
from code.ACCOUNT_TYPE import ACCOUNT_TYPE
from common.MiralLogger import MiralLogger
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralMsgTbl import MiralMsgTbl



class AccountMsg(messages.Message):
    u"""アカウントメッセージ"""
    email = messages.StringField(2)                                       #EMailアドレス
    acType = messages.IntegerField(3)                                     #アカウント種別
    lastName = messages.StringField(4)                                    #氏名(苗字)
    firstName = messages.StringField(5)                                   #氏名(名前)
    lastNameKana = messages.StringField(6)                                #氏名カナ(苗字)
    firstNameKana = messages.StringField(7)                               #氏名カナ(名前)
    prefecturesCd = messages.IntegerField(8)                              #都道府県コード
    tell = messages.StringField(9)                                        #電話番号
    passWord = messages.StringField(10)                                   #パスワード
    facebookId = messages.StringField(16)                                 #FacebookID
    facebookToke = messages.StringField(17)                               #FacebookToken
    twitterId = messages.StringField(18)                                  #TwitterId   
    twitterToken = messages.StringField(19)                               #TwitterToken  
    googleplusId = messages.StringField(20)                               #googleId   
    googleplusToken = messages.StringField(21)                            #googleToken      
    instagramId = messages.StringField(22)                                #instagramId   
    instagramToken = messages.StringField(23)                             #instagramToken

    accountId = messages.StringField(24)                                  #アカウントId

class AccountGetMsg(messages.Message):
    u"""アカウント取得依頼メッセージ"""
    loginType = messages.IntegerField(1)           #ログインタイプ
    id = messages.StringField(2)                   #識別ID

class AccountGetResMsg(messages.Message):
    u"""アカウント取得結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    account = messages.MessageField(AccountMsg, 2)      #アカウント情報



class AccountService():
    u"""アカウントサービス"""
    
    def get(self, loginType_, id_):
        u"""アカウント情報取得"""
        
        logger = MiralLogger()

        logger.debug('get ' + str(loginType_) + ' ' + str(LOGIN_TYPE.facebook.getCode()))
        
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

        accountMsg =  AccountMsg()
        
        if not accountKnd:
            logger.debug("loginType:"+str(loginType_) +" id:"+id_+u" は存在しません")
            accountMsg.res = ApiResponceMsg(rstCode=UMU_FLG.nasi.getCode())
            return accountMsg
        
        
        self.__covKnd2Msg(accountKnd, accountMsg)

        resMsg = AccountGetResMsg()
        
        resMsg.res = ApiResponceMsg(rstCode=UMU_FLG.ari.getCode())
        resMsg.account = accountMsg 
        return resMsg
    
    def isEmailExists(self, email_):
        acq = AccountKind.query(AccountKind.email == email_)
        existAccountKnd = acq.get(keys_only=True)
        if existAccountKnd:
            return True
        
        return False
    
    
    def add(self, accountMsg_):
        
        logger = MiralLogger()
        
        accountKnd = AccountKind()
        
        self.__covMsg2Knd(accountMsg_, accountKnd) 
        
        accountKnd.put()
        
        logger.debug("AccountService add ok!")
        return accountKnd.key
        
    
    def __covKnd2Msg(self, k_, m_):
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
        
        m_.accountId = str(k_.key.id())            
        
    def __covMsg2Knd(self, m_, k_):
        k_.email = m_.email                            #EMailアドレス
        k_.acType = m_.acType                          #アカウント種別
        k_.lastName = m_.lastName                      #氏名(苗字)
        k_.firstName = m_.firstName                    #氏名(名前)
        k_.lastNameKana = m_.lastNameKana              #氏名カナ(苗字)
        k_.firstNameKana = m_.firstNameKana            #氏名カナ(名前)
        k_.prefecturesCd = m_.prefecturesCd            #都道府県
        k_.tell = m_.tell                              #電話番号
        k_.passWord = m_.passWord                      #パスワード
        k_.facebookId = m_.facebookId                  #FacebookID
        k_.facebookToke = m_.facebookToke              #FacebookToken
        k_.twitterId = m_.twitterId                    #TwitterId   
        k_.twitterToken = m_.twitterToken              #TwitterToken  
        k_.googleplusId = m_.googleplusId              #googleId   
        k_.googleplusToken = m_.googleplusToken        #googleToken      
        k_.instagramId = m_.instagramId                #instagramId   
        k_.instagramToken = m_.instagramToken          #instagramToken
        
          
            