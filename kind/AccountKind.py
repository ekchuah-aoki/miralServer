
from google.appengine.ext import ndb
from kind import BaseKind

class AccountKind(BaseKind):
    """アカウント情報"""
    email = ndb.StringProperty(index=True)                            #EMailアドレス
    knd = ndb.IntegerProperty()                                       #アカウント種別
    lastName = ndb.StringProperty()                                   #氏名(苗字)
    firstName = ndb.StringProperty()                                  #氏名(名前)
    prefecturesCd = ndb.IntegerProperty()                             #都道府県
    tell = ndb.StringProperty()                                       #電話番号
    passWord = ndb.StringProperty()                                   #パスワード
    totalPoint = ndb.IntegerProperty(default=0)                       #所有合計ポイント
