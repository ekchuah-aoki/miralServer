# coding: UTF-8
from protorpc import messages
from common.msg.ApiResponceMsg import ApiResponceMsg
class BeautiImageResMsg(messages.Message):
    u"""アカウントメッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)
    imgUrl = messages.StringField(2) 