# coding: UTF-8

from beauti.BeautiImage import BeautiImage
from common.ImageUtil import ImageUtil
from google.appengine.ext import ndb
from kind.MessageThreadKind import MessageThreadKind
from kind.MessageContactKind import MessageContactKind
from code.OK_NG import OK_NG
from code.MSG_SENDER import MSG_SENDER
from common.msg.ApiResponceMsg import ApiResponceMsg
from beauti.msg import BeautiImageGetResMsg
from common.MiralLogger import MiralLogger

class MessageService():
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
            
        
        