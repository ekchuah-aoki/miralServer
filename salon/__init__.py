"""
google data store kind定義

AccountKInd アカウント情報

"""
from google.appengine.ext import ndb

class AccountKind(ndb.Model):
    email = ndb.StringProperty(indexed=True)    #e-mailアドレス
    last_name = ndb.StringProperty()            #氏名（苗字）
    pw_hash = ndb.StringProperty()              #氏名（名前）

