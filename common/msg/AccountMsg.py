# coding: UTF-8
from protorpc import messages
from common.msg.ApiResponceMsg import ApiResponceMsg
class AccountMsg(messages.Message):
    u"""アカウントメッセージ"""
    
    res = messages.MessageField(ApiResponceMsg, 1)
    
    email = messages.StringField(2)                                       #EMailアドレス
    acType = messages.IntegerField(3)                                     #アカウント種別
    lastName = messages.StringField(4)                                    #氏名(苗字)
    firstName = messages.StringField(5)                                   #氏名(名前)
    lastNameKana = messages.StringField(6)                                #氏名カナ(苗字)
    firstNameKana = messages.StringField(7)                               #氏名カナ(名前)
    prefecturesCd = messages.IntegerField(8)                              #都道府県コード
    tell = messages.StringField(9)                                        #電話番号
    passWord = messages.StringField(10,)                                  #パスワード
    totalPoint = messages.IntegerField(11,default=0)                      #所有合計ポイント
    gender = messages.IntegerField(12)                                    #性別
    birthday_y = messages.StringField(13)                                 #生年月日 年
    birthday_m = messages.StringField(14)                                 #生年月日 年
    birthday_d = messages.StringField(15)                                 #生年月日 年
    facebookId = messages.StringField(16)                                 #FacebookID
    facebookToke = messages.StringField(17)                               #FacebookToken
    twitterId = messages.StringField(18)                                  #TwitterId   
    twitterToken = messages.StringField(19)                               #TwitterToken  
    googleplusId = messages.StringField(20)                                   #googleId   
    googleplusToken = messages.StringField(21)                                #googleToken      
    instagramId = messages.StringField(22)                                #instagramId   
    instagramToken = messages.StringField(23)                             #instagramToken

    accountId = messages.StringField(24)                                     #アカウントId
