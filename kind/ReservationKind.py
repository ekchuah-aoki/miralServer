# coding: UTF-8

from google.appengine.ext import ndb
from kind.BaseKind import BaseKind
from kind.AccountKind import AccountKind
from kind.MessageThreadKind import MessageThreadKind

class ReservationKind(BaseKind):
    u"""予約情報"""
    rsvSalonKey = ndb.KeyProperty(kind=AccountKind)                     #予約サロンKey
    rsvbeautiKey = ndb.KeyProperty(kind=AccountKind)               #予約美容師Key
    apptDate = ndb.DateProperty()                                     #予約日
    apptType = ndb.IntegerProperty()                                   #予約種類
    apptStartTime = ndb.TimeProperty()                                #予約開始時刻
    apptEndTime = ndb.TimeProperty()                                  #予約終了時刻
    apptPoint = ndb.IntegerProperty()                                 #予約ポイント
    cancelPoint = ndb.IntegerProperty()                               #キャンセルポイント
    messageThreadKey = ndb.KeyProperty(kind=MessageThreadKind)        #メッセージスレッドKey
    cancelReqTime = ndb.DateTimeProperty()                            #キャンセル依頼日時
    cancelTime = ndb.DateTimeProperty()                               #キャンセル確定日時
