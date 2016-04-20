# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind

class AccountKind(BaseKind):
    u"""アカウント情報"""
    email = ndb.StringProperty(indexed=True)                            #EMailアドレス
    acType = ndb.IntegerProperty()                                       #アカウント種別
    lastName = ndb.StringProperty()                                   #氏名(苗字)
    firstName = ndb.StringProperty()                                  #氏名(名前)
    lastNameKana = ndb.StringProperty()                                   #氏名カナ(苗字)
    firstNameKana = ndb.StringProperty()                                  #氏名カナ(名前)
    prefecturesCd = ndb.IntegerProperty()                             #都道府県
    tell = ndb.StringProperty()                                       #電話番号
    passWord = ndb.StringProperty()                                   #パスワード
    totalPoint = ndb.IntegerProperty(default=0)                       #所有合計ポイント
    gender = ndb.IntegerProperty()                                    #性別
    birthday = ndb.DateProperty()                                     #生年月日
    imageData = ndb.StringProperty()                                    #画像
    
    facebookId = ndb.StringProperty(indexed=True)                       #FacebookID
    facebookToke = ndb.StringProperty()                               #FacebookToken
    twitterId = ndb.StringProperty(indexed=True)                        #TwitterId   
    twitterToken = ndb.StringProperty()                               #TwitterToken  
    googleplusId = ndb.StringProperty(indexed=True)                         #googleId   
    googleplusToken = ndb.StringProperty()                                #googleToken      
    instagramId = ndb.StringProperty(indexed=True)                      #instagramId   
    instagramToken = ndb.StringProperty()                             #instagramToken          