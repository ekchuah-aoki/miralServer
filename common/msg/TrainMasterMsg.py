# coding: UTF-8
from protorpc import messages
from common.msg.ApiResponceMsg import ApiResponceMsg

class TrainListItemMsg(messages.Message):
    u"""路線リストメッセージ"""
    trainCd = messages.IntegerField(1)                        #路線コード
    trainName   = messages.StringField(2)                     #路線名

class TrainMasterGetTrainListMsg(messages.Message):
    u"""路線リスト取得依頼メッセージ"""
    pos = messages.IntegerField(1)              #読み込み開始位置（1から）
    limit=messages.IntegerField(2)              #読込数
                  
class TrainMasterGetTrainListResMsg(messages.Message):
    u"""路線リスト取得結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)
    trains = messages.MessageField(TrainListItemMsg, 2, repeated=True)
