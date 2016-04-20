# coding: UTF-8
from protorpc import messages

class ApiParamMsg(messages.Message):
    u"""アカウントメッセージ"""
    param = messages.StringField(1,repeated=True)           #パラメータ
