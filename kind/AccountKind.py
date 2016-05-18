# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.BeauticianKind import BeauticianKind
from kind.SalonKind import SalonKind

class AccountKind(BaseKind):
    u"""アカウント情報"""
    email = ndb.StringProperty(indexed=True)                          #EMailアドレス
    acType = ndb.IntegerProperty()                                    #アカウント種別
    lastName = ndb.StringProperty()                                   #氏名(苗字)
    firstName = ndb.StringProperty()                                  #氏名(名前)
    lastNameKana = ndb.StringProperty()                               #氏名カナ(苗字)
    firstNameKana = ndb.StringProperty()                              #氏名カナ(名前)
    prefecturesCd = ndb.IntegerProperty()                             #都道府県
    tell = ndb.StringProperty()                                       #電話番号
    passWord = ndb.StringProperty()                                   #パスワード
    
    facebookId = ndb.StringProperty(indexed=True)                     #FacebookID
    facebookToke = ndb.StringProperty()                               #FacebookToken
    twitterId = ndb.StringProperty(indexed=True)                      #TwitterId   
    twitterToken = ndb.StringProperty()                               #TwitterToken  
    googleplusId = ndb.StringProperty(indexed=True)                   #googleId   
    googleplusToken = ndb.StringProperty()                            #googleToken      
    instagramId = ndb.StringProperty(indexed=True)                    #instagramId   
    instagramToken = ndb.StringProperty()                             #instagramToken
    
    beautiKey = ndb.KeyProperty(kind=BeauticianKind)                  #美容師Key
    salonKey = ndb.KeyProperty(kind=SalonKind)                        #サロンKey
    
    temporary = ndb.BooleanProperty(default=True)                   #仮登録フラグ  