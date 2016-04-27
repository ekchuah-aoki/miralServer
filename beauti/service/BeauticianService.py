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
from code.MSG_SENDER import MSG_SENDER
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralLogger import MiralLogger
from common.DateUtil import DateUtil
from common.service.AccountService import AccountService
from common.service.AccountService import AccountMsg

class BeauticianMsg(messages.Message):
    u"""美容師メッセージ"""
    accountId = messages.StringField(1)                 #アカウントId
    nickName = messages.StringField(2)                  #ニックネーム
    compEval = messages.FloatField(3)                   #総合評価
    pr = messages.IntegerField(4)                       #自己PR
    totalPoint = messages.IntegerField(5)               #所有合計ポイント
    gender = messages.IntegerField(6)                   #性別

    birthday_y = messages.StringField(7)                #生年月日 年
    birthday_m = messages.StringField(8)                #生年月日 年
    birthday_d = messages.StringField(9)                #生年月日 年
    
    licenseFlg = messages.StringField(10)               #美容師免許承認済みフラグ
    srhCondPref = messages.IntegerField(11)             #検索対象都道府県
    srhCondIowestRat = messages.FloatField(12)          #検索対象最低総合評価
    
class BeautiAccountAddMsg(messages.Message):
    u"""美容師アカウント新規登録依頼メッセージ"""
    account = messages.MessageField(AccountMsg, 1)      #アカウント情報
    beautician = messages.MessageField(BeauticianMsg, 2) #美容師情報

class BeautiAccountAddResMsg(messages.Message):
    u"""美容師アカウント新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    kindId = messages.StringField(2)                    #KindID

class BeauticianService():
    
    _SETMODE = {"account":1,
                "profile":2,
                "other":3} 
    
    @ndb.transactional(xg=True)    
    def _add(self, accountBeautiAddMsg_):
       
        #アカウント情報登録
        accountService = AccountService()
        accountKey = accountService.add(accountBeautiAddMsg_.account)
        
        #美容師情報登録
        beautiKnd = BeauticianKind()
        beautiKnd.accountKey = accountKey
        beautiKnd.gender = accountBeautiAddMsg_.beautician.gender                                    #性別
        beautiKnd.birthday = DateUtil.getDateByStr(accountBeautiAddMsg_.beautician.birthday_y
                                                   ,accountBeautiAddMsg_.beautician.birthday_m
                                                   ,accountBeautiAddMsg_.beautician.birthday_d)             #生年月日
        
        beautiKnd.put();
        
        
        return beautiKnd.key;
 
    def add(self, accountBeautiAddMsg_):
        u"""美容師新規登録"""
        
        logger = MiralLogger()
        
        accountService = AccountService()
        resMsg = BeautiAccountAddResMsg()
        
        #アカウント（Email)の存在チェック
        if accountService.isEmailExists(accountBeautiAddMsg_.account.email):
            resMsg.res = ApiResponceMsg(rstCode=OK_NG.ng.getCode())
            return resMsg

        beautiKey = self._add(accountBeautiAddMsg_)
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        logger.debug("--------- BeauticianService add!"+str(beautiKey.id()))
        resMsg.kindId = str(beautiKey.id())

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
            
        
    def __covMsg2Knd(self, m_, k_, setMode_):
        k_.accountKey = ndb.Key("AccountKind", m_.accountId)              #アカウントKey
        k_.nickName = ndb.StringProperty()                                   #ニックネーム
        pr = ndb.IntegerProperty()                                        #自己PR
        #k_.compEval = ndb.FloatProperty()                                    #総合評価
        #totalPoint = ndb.IntegerProperty(default=0)                       #所有合計ポイント
        gender = ndb.IntegerProperty()                                    #性別
        birthday = ndb.DateProperty()                                     #生年月日
        licenseFlg = ndb.TextProperty()                                   #美容師免許承認済みフラグ
        srhCondPref = ndb.IntegerProperty(repeated=True)                  #検索対象都道府県
        srhCondIowestRat = ndb.FloatProperty()                            #検索対象最低総合評価
        #BeauticianMyGalleryKeyList = ndb.KeyProperty(repeated=True,"kind=BeauticianMyGalleryKind")     #プロフィール画像
        #BeauticianWorkGalleryKeyList = ndb.KeyProperty(repeated=True,"kind=BeauticianWorkGalleryKind") #実績画像
      
      
      
      
      
         