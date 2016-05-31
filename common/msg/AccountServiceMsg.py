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

    temporary = messages.BooleanField(24)                                 #仮登録中  
    accountId    = messages.StringField(25)                               #アカウントId
    kindId = messages.StringField(26)                                       #容師の場合は美容師KindのId、サロンの場合はサロンのKindのId 

class AccountGetMsg(messages.Message):
    u"""アカウント取得依頼メッセージ"""
    loginType = messages.IntegerField(1)           #ログインタイプ
    id = messages.StringField(2)                   #識別ID

class AccountGetResMsg(messages.Message):
    u"""アカウント取得結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    account = messages.MessageField(AccountMsg, 2)      #アカウント情報


class AccountGetLoginMsg(messages.Message):
    u"""アカウント取得依頼メッセージ"""
    loginType = messages.IntegerField(1)           #ログインタイプ
    id = messages.StringField(2)                   #識別ID
    pwd = messages.StringField(3)                  #パスワード（E-mailの場合のみ)

class AccountGetLoginResMsg(messages.Message):
    u"""アカウント取得結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    accountId  = messages.StringField(2)                               #アカウントId
    kindId = messages.StringField(3)                                   #容師の場合は美容師KindのId、サロンの場合はサロンのKindのId 

    email = messages.StringField(4)                                       #EMailアドレス
    acType = messages.IntegerField(5)                                     #アカウント種別
    lastName = messages.StringField(6)                                    #氏名(苗字)
    firstName = messages.StringField(7)                                   #氏名(名前)
    temporary = messages.BooleanField(8)                                 #仮登録中  

            