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

class BeautiTempAccountAddMsg(messages.Message):
    u"""美容師アカウント仮登録依頼メッセージ"""
    email = messages.StringField(1)                                       #EMailアドレス
    acType = messages.IntegerField(2)                                     #アカウント種別
    lastName = messages.StringField(3)                                    #氏名(苗字)
    firstName = messages.StringField(4)                                   #氏名(名前)
    lastNameKana = messages.StringField(5)                                #氏名カナ(苗字)
    firstNameKana = messages.StringField(6)                               #氏名カナ(名前)
    prefecturesCd = messages.IntegerField(7)                              #都道府県コード
    tell = messages.StringField(8)                                        #電話番号
    passWord = messages.StringField(9)                                   #パスワード
    facebookId = messages.StringField(10)                                 #FacebookID
    facebookToke = messages.StringField(11)                               #FacebookToken
    twitterId = messages.StringField(12)                                  #TwitterId   
    twitterToken = messages.StringField(13)                               #TwitterToken  

class BeautiTempAccountAddResMsg(messages.Message):
    u"""美容師アカウント仮登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    accountId = messages.StringField(2)                 #アカウントId
    kindId = messages.StringField(3)                   #容師の場合は美容師KindのId、サロンの場合はサロンのKindのId 


class BeauticianAccountEditMsg(messages.Message):
    u"""美容師アカウント情報編集メッセージ"""
    
    email = messages.StringField(1)                         #EMailアドレス
    lastName = messages.StringField(2)                      #氏名(苗字)
    firstName = messages.StringField(3)                     #氏名(名前)
    lastNameKana = messages.StringField(4)                  #氏名カナ(苗字)
    firstNameKana = messages.StringField(5)                 #氏名カナ(名前)
    prefecturesCd = messages.IntegerField(6)                #都道府県コード
    tell = messages.StringField(7)                          #電話番号
    passWord = messages.StringField(8)                      #パスワード
    
    gender = messages.IntegerField(9)                       #性別
    birthday_y = messages.StringField(10)                   #生年月日 年
    birthday_m = messages.StringField(11)                   #生年月日 月
    birthday_d = messages.StringField(12)                   #生年月日 日
    licenseFlg = messages.StringField(13)                   #美容師免許承認済みフラグ

    temporary = messages.BooleanField(14)                   #一時保存フラグ

class BeauticianGetAccountMsg(messages.Message):
    accountId = messages.StringField(1)                         #アカウントId

class BeauticianGetAccount4EditResMsg(messages.Message):
    res = messages.MessageField(ApiResponceMsg, 1)                  #結果
    beauti = messages.MessageField(BeauticianAccountEditMsg, 2)     #アカウント情報

class BeauticianModityAccountMsg(messages.Message):
    accountId = messages.StringField(1)                         #アカウントId
    beauti = messages.MessageField(BeauticianAccountEditMsg, 2)     #アカウント情報
    
class BeauticianModityAccountResMsg(messages.Message):
    res = messages.MessageField(ApiResponceMsg, 1)                  #結果


######################################################
class BeauticianMsg(messages.Message):
    u"""美容師メッセージ"""
    nickName = messages.StringField(2)                  #ニックネーム
    compEval = messages.FloatField(3)                   #総合評価
    pr = messages.IntegerField(4)                       #自己PR
    totalPoint = messages.IntegerField(5)               #所有合計ポイント
    gender = messages.IntegerField(6)                   #性別

    birthday_y = messages.StringField(7)                #生年月日 年
    birthday_m = messages.StringField(8)                #生年月日 月
    birthday_d = messages.StringField(9)                #生年月日 日
    licenseFlg = messages.StringField(10)               #美容師免許承認済みフラグ
    
class BeauticianOtherMsg(messages.Message):
    srhCondPref = messages.IntegerField(11)             #検索対象都道府県
    srhCondIowestRat = messages.FloatField(12)          #検索対象最低総合評価

    
class BeautiAccountAddMsg(messages.Message):
    u"""美容師アカウント新規登録依頼メッセージ"""
    account = messages.MessageField(AccountMsg, 1)      #アカウント情報
    beautician = messages.MessageField(BeauticianMsg, 2) #美容師情報

class BeautiAccountAddResMsg(messages.Message):
    u"""美容師アカウント新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    accountId = messages.StringField(2)                    #アカウントId




class BeautiAccountModifyMsg(messages.Message):
    u"""美容師アカウント新規登録依頼メッセージ"""
    account = messages.MessageField(AccountMsg, 1)      #アカウント情報
    beautician = messages.MessageField(BeauticianMsg, 2) #美容師情報

class BeautiAccountModifyResMsg(messages.Message):
    u"""美容師アカウント新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果

class BeautiGetAccountInfoMsg(messages.Message):
    u"""美容師アカウント情報取得依頼メッセージ"""
    accountId = messages.StringField(1)      #アカウントId


class BeautiGetAccountInfoResMsg(messages.Message):
    u"""美容師アカウント情報取得結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    account = messages.MessageField(AccountMsg, 2)       #アカウント情報
    beautician = messages.MessageField(BeauticianMsg, 3) #美容師情報

