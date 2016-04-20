# coding: UTF-8
from protorpc import messages

class BeautiImageMsg(messages.Message):
    u"""アカウントメッセージ"""
    accountId = messages.StringField(1)                 #アカウントID
    imgbase64data = messages.StringField(2)              #イメージデータ