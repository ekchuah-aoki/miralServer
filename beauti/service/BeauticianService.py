# coding: UTF-8
from protorpc import messages
from google.appengine.ext import ndb

from beauti.BeautiImage import BeautiImage
from common.ImageUtil import ImageUtil
from google.appengine.ext import ndb
from kind.BeauticianKind import BeauticianKind
from kind.MessageThreadKind import MessageThreadKind
from kind.MessageContactKind import MessageContactKind
from code.OK_NG import OK_NG
from code.ACCOUNT_TYPE import ACCOUNT_TYPE
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralLogger import MiralLogger
from common.DateUtil import DateUtil
from common.service.AccountService import AccountService
from common.service.AccountService import AccountMsg
from common.CommUtil import CommUtil

from kind.AccountKind import AccountKind


from beauti.msg.BeauticianServiceMsg import BeautiTempAccountAddResMsg
from beauti.msg.BeauticianServiceMsg import BeauticianAccountEditMsg
from beauti.msg.BeauticianServiceMsg import BeauticianGetAccountMsg
from beauti.msg.BeauticianServiceMsg import BeauticianGetAccount4EditResMsg
from beauti.msg.BeauticianServiceMsg import BeauticianModityAccountResMsg

from beauti.msg.BeauticianServiceMsg import  BeauticianOtherMsg 
from beauti.msg.BeauticianServiceMsg import  BeautiAccountAddMsg
from beauti.msg.BeauticianServiceMsg import  BeautiAccountAddResMsg
from beauti.msg.BeauticianServiceMsg import  BeautiAccountModifyMsg
from beauti.msg.BeauticianServiceMsg import  BeautiAccountModifyResMsg
 
class BeauticianService():

    @ndb.transactional(xg=True)
    def __addTemp(self, tempAddMsg_):
        u"""仮新規新規登録"""
        
        #美容師情報登録
        #仮登録では空
        beautiKnd = BeauticianKind()
        beautiKnd.put()

        #アカウント情報登録
        accountKnd = AccountKind()
        accountKnd.beautiKey = beautiKnd.key
        accountKnd.email = tempAddMsg_.email                            #EMailアドレス
        accountKnd.acType = ACCOUNT_TYPE.beauti.getCode()               #アカウント種別
        accountKnd.facebookId = tempAddMsg_.facebookId                  #FacebookID
        accountKnd.twitterId = tempAddMsg_.twitterId                    #TwitterId   
         
        accountKnd.lastName = tempAddMsg_.lastName                      #氏名(苗字)
        accountKnd.firstName = tempAddMsg_.firstName                    #氏名(名前)
        accountKnd.lastNameKana = tempAddMsg_.lastNameKana              #氏名カナ(苗字)
        accountKnd.firstNameKana = tempAddMsg_.firstNameKana            #氏名カナ(名前)
        
        accountKnd.temporary = True                                     #仮登録フラグ
         
        accountKnd.put()
                
        return accountKnd
        
    
         
    def addTempAccount(self, tempAddMsg_):
        u"""アカウント仮登録"""
        logger = MiralLogger()
        
        accountService = AccountService()
        resMsg = BeautiTempAccountAddResMsg()
        
        #アカウント（Email)の存在チェック
        if accountService.isEmailExists(tempAddMsg_.email):
            resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
            return resMsg

        #仮登録
        accountKnd = self.__addTemp(tempAddMsg_)
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        logger.debug("--------- BeauticianService addTemp!"+str(accountKnd.key.id()))
        resMsg.accountId = str(accountKnd.key.id())
        resMsg.kindId = str(accountKnd.beautiKey.id())

        return resMsg    


    def getAccount4Edit(self, reqMsg_):
        logger = MiralLogger()
        logger.debug("--------- BeauticianService getAccount4Edit start!")        
        
        
        accMsg = BeauticianAccountEditMsg()                 
        accountKey = ndb.Key(AccountKind, long(reqMsg_.accountId))
        accountKnd = accountKey.get()


        accMsg.email = accountKnd.email                            #EMailアドレス
         
        accMsg.lastName = accountKnd.lastName                      #氏名(苗字)
        accMsg.firstName = accountKnd.firstName                    #氏名(名前)
        accMsg.lastNameKana = accountKnd.lastNameKana              #氏名カナ(苗字)
        accMsg.firstNameKana = accountKnd.firstNameKana            #氏名カナ(名前)
        accMsg.prefecturesCd = accountKnd.prefecturesCd            #都道府県
        accMsg.tell = accountKnd.tell                              #電話番号
        
        accMsg.temporary = accountKnd.temporary                    #仮登録フラグ
        
        beautiKnd = accountKnd.beautiKey.get()
        accMsg.gender = beautiKnd.gender                      #性別
        
        if beautiKnd.birthday:
            accMsg.birthday_y = str(beautiKnd.birthday.year)              #生年月日 年
            accMsg.birthday_m = str(beautiKnd.birthday.month)              #生年月日 月
            accMsg.birthday_d = str(beautiKnd.birthday.day)              #生年月日 日
        
        accMsg.licenseFlg = beautiKnd.licenseFlg              #美容師免許承認済みフラグ
        resMsg = BeauticianGetAccount4EditResMsg()
        resMsg.beauti = accMsg
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
        
        return resMsg
    
    @ndb.transactional(xg=True)    
    def __modifyAccount(self, reqMsg_):
        logger = MiralLogger()
        logger.debug("__modifyAccount")


        #アカウント情報
        accountKey = ndb.Key(AccountKind, long(reqMsg_.accountId))
        accountKnd = accountKey.get()

        accountKnd.email = reqMsg_.beauti.email                        #EMailアドレス
         
        accountKnd.lastName = reqMsg_.beauti.lastName                      #氏名(苗字)
        accountKnd.firstName = reqMsg_.beauti.firstName                    #氏名(名前)
        accountKnd.lastNameKana = reqMsg_.beauti.lastNameKana              #氏名カナ(苗字)
        accountKnd.firstNameKana = reqMsg_.beauti.firstNameKana            #氏名カナ(名前)
        accountKnd.prefecturesCd = reqMsg_.beauti.prefecturesCd            #都道府県
        accountKnd.tell = reqMsg_.beauti.tell                              #電話番号
        
        #修正ということは、正規登録。
        accountKnd.temporary = False

        if reqMsg_.beauti.passWord:
            accountKnd.passWord = reqMsg_.beauti.passWord

        accountKnd.put()

        #美容師情報
        beautiKnd = accountKnd.beautiKey.get()
        
        beautiKnd.gender = reqMsg_.beauti.gender                      #性別
        
        if reqMsg_.beauti.birthday_y:
            beautiKnd.birthday = DateUtil.getDateByStr(reqMsg_.beauti.birthday_y
                                                       ,reqMsg_.beauti.birthday_m
                                                       ,reqMsg_.beauti.birthday_d)             #生年月日
            
        
        beautiKnd.put()
        
        return
    
    def modify(self, reqMsg_):
        u"""アカウント情報の変更"""
        logger = MiralLogger()
        logger.debug("--------- BeauticianService modify!"+reqMsg_.accountId)
    
        resMsg = BeauticianModityAccountResMsg()
    
        #アカウント（Email)の存在チェック
        accountService = AccountService()
        if accountService.isEmailExists(reqMsg_.beauti.email, reqMsg_.accountId):
            resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
            return resMsg

        #修正
        self.__modifyAccount(reqMsg_)
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())

        return resMsg    
        
    ###########################################################################################    
    


    def __covMsg2Knd(self, k_, m_):
        k_.gender = m_.beautician.gender                                    #性別
        
        k_.birthday = DateUtil.getDateByStr(m_.beautician.birthday_y
                                                   ,m_.beautician.birthday_m
                                                   ,m_.beautician.birthday_d)             #生年月日


    def getKind(self, id_):
        beautiKey = ndb.Key(BeauticianKind, id_)
        
        return beautiKey.get()    
        
        
    @ndb.transactional(xg=True)    
    def __addAccount(self, reqMsg_):
        #美容師情報登録
        beautiKnd = BeauticianKind()

        self.__covMsg2Knd(beautiKnd, reqMsg_)
        beautiKnd.put()

        #アカウント情報登録
        accountKnd = AccountKind()
        accountKnd.email = reqMsg_.beautician.email                            #EMailアドレス
        accountKnd.acType = ACCOUNT_TYPE.beauti.getCode()                       #アカウント種別
        #accountKnd.facebookId = reqMsg_.facebookId                              #FacebookID
        #accountKnd.facebookToke = reqMsg_.facebookToke                          #FacebookToken
        #accountKnd.twitterId = reqMsg_.twitterId                                #TwitterId   
        #accountKnd.twitterToken = reqMsg_.twitterToken                          #TwitterToken  
        #accountKnd.googleplusId = reqMsg_.beautician.googleplusId              #googleId   
        #accountKnd.googleplusToken = reqMsg_.beautician.googleplusToken        #googleToken      
        #accountKnd.instagramId = reqMsg_.beautician.instagramId                #instagramId   
        #accountKnd.instagramToken = reqMsg_.beautician.instagramToken          #instagramToken
         
        accountKnd.lastName = reqMsg_.beautician.lastName                       #氏名(苗字)
        accountKnd.firstName = reqMsg_.beautician.firstName                     #氏名(名前)
        accountKnd.lastNameKana = reqMsg_.beautician.lastNameKana               #氏名カナ(苗字)
        accountKnd.firstNameKana = reqMsg_.beautician.firstNameKana             #氏名カナ(名前)
        accountKnd.prefecturesCd = reqMsg_.beautician.prefecturesCd             #都道府県
        accountKnd.tell = reqMsg_.beautician.tell                               #電話番号
        accountKnd.passWord = reqMsg_.beautician.passWord                       #パスワード
        
        accountKnd.temporary = False                                            #仮登録フラグ
        
        accountKnd.beautiKey = beautiKnd.key
        
        accountKnd.put()
        
        return accountKnd
 
        
    def add(self, accountBeautiAddMsg_):
        u"""美容師新規登録"""
        
        logger = MiralLogger()
        
        accountService = AccountService()
        resMsg = BeautiAccountAddResMsg()
        
        #アカウント（Email)の存在チェック
        if accountService.isEmailExists(accountBeautiAddMsg_.beautician.email):
            resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
            return resMsg

       
        accountKnd = self.__addAccount(accountBeautiAddMsg_)
        
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        logger.debug("--------- BeauticianService add!"+str(accountKnd.beautiKey.id()))
        resMsg.accountId = str(accountKnd.key.id())
        resMsg.kindId = str(accountKnd.beautiKey.id())

        return resMsg    
    
     
    
    def addContact(self, threadId_, senderType_, comment_):
        u""" メッセージ情報の登録 """
        msgThreadKey = ndb.Key('MessageThreadKind', threadId_)
        
        msgContactKnd = MessageContactKind()
        msgContactKnd.direct = senderType_
        msgContactKnd.comment = threadId_
        msgContactKnd.messageKey = msgThreadKey
        msgContactKnd.put()
        
        resMsg = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        return resMsg
        
    @ndb.transactional        
    def addThread(self, msgType_, senderTYpe_, senderId_, receiverId_, caption_, comment_, matchId_):

        u"""メッセージスレッド情報の登録、同時に初期のメッセージ情報を登録する"""
        

        #スレッドを追加
        msgThreadKnd = MessageThreadKind()
        msgThreadKnd.caption = caption_
        
        msgThreadKnd.senderKey = senderId_
        msgThreadKnd.receiverKey = receiverId_
        
        if not matchId_:
            matchKey = ndb.Key("MatchingKind", matchId_)
            msgThreadKnd.matchingKey = matchKey
            
        msgThreadKnd.put()

        #初期コンタクト追加        
        self.addContact(msgThreadKnd.key.id, senderTYpe_, comment_)
        resMsg = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        return resMsg
       
    def getThread(self, accountId_, type_):
        return BeautiImage.getImageData(accountId_, type_)
            
