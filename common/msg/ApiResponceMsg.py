# coding: UTF-8
from protorpc import messages

class ApiResponceMsg(messages.Message):
    u"""API レスポンスメッセージ"""
    rstCode = messages.IntegerField(1)                      #コード
    rstMsg = messages.StringField(2, default="")            #メッセージ
    
