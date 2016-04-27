# coding: UTF-8
from protorpc import messages
from common.msg.ApiResponceMsg import ApiResponceMsg
class ImageResMsg(messages.Message):
    u"""画像データ（Base64）メッセージ"""
    accountId = messages.StringField(1)         #アカウントId
    startDate = messages.StringField(2)         #取得対象開始日（yyyymmdd）
    startPos  = messages.IntegerField(3)        #startポジション
    endPos    = messages.IntegerField(4)        #endポジション