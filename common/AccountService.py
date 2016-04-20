# coding: UTF-8
from kind.AccountKind import AccountKind
from code.LOGIN_TYPE import LOGIN_TYPE
from code.OK_NG import OK_NG
from code.UMU_FLG import UMU_FLG
from common.MiralLogger import MiralLogger
from common.msg.AccountMsg import AccountMsg
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralMsgTbl import MiralMsgTbl
from datetime import date

class AccountService():
    u"""アカウントサービス"""
    
    def get(self, loginType_, id_):
        
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
        accountMsg.res = ApiResponceMsg(rstCode=UMU_FLG.ari.getCode())
            
        return accountMsg
    
    def add(self, accountMsg_):
        
        logger = MiralLogger()
        
        acq = AccountKind.query(AccountKind.email == accountMsg_.email)
        existAccountKnd = acq.get()
        if existAccountKnd:
            accountMsg_.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode(), rstMsg=MiralMsgTbl.MSG_COMMON_0001 )
            logger.debug("add ng!")
            return accountMsg_
        
        accountKnd = AccountKind()
        
        self.__covMsg2Knd(accountMsg_, accountKnd) 
        
        accountKnd.put()
        accountMsg_.accountId = str(accountKnd.key.id()) 
        accountMsg_.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        logger.debug("add ok!")
        return accountMsg_
        
    
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
        m_.gender = k_.gender                          #性別
        if not k_.birthday:
            m_.birthday_y = k_.birthday.strftime("%Y")                       #生年月日
            m_.birthday_m = k_.birthday.strftime("%m")                       #生年月日
            m_.birthday_d = k_.birthday.strftime("%d")                       #生年月日
        m_.totalPoint = k_.totalPoint                  #所有合計ポイント
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
        k_.gender = m_.gender                          #性別
        if m_.birthday_y != "":
            k_.birthday = date(int(m_.birthday_y), int(m_.birthday_m),int(m_.birthday_d))                      #生年月日
        k_.totalPoint = m_.totalPoint                  #所有合計ポイント
        k_.facebookId = m_.facebookId                  #FacebookID
        k_.facebookToke = m_.facebookToke              #FacebookToken
        k_.twitterId = m_.twitterId                    #TwitterId   
        k_.twitterToken = m_.twitterToken              #TwitterToken  
        k_.googleplusId = m_.googleplusId              #googleId   
        k_.googleplusToken = m_.googleplusToken        #googleToken      
        k_.instagramId = m_.instagramId                #instagramId   
        k_.instagramToken = m_.instagramToken          #instagramToken
        
          
            