# coding: UTF-8
from protorpc import messages
from common.msg.ApiResponceMsg import ApiResponceMsg
class ImageResMsg(messages.Message):
    u"""画像データ（Base64）メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)
    msgType = messages.IntegerField(2)              #メセージタイプ
    caption = messages.StringField(3)               #キャプション
    receThImgFilename = messages.StringField(4)     #相手サムネイル画像ファイル名
    receName = messages.StringField(5)              #相手名
    shortMsg = messages.StringField(6)              #ショートメッセージ
    senderTime = messages.StringField(7)            #最終送信日時
    msgThreadId = messages.StringField(8)           #メッセージスレッドId
