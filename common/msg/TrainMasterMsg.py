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


class StationListItemMsg(messages.Message):
    u"""駅リストメッセージ"""
    stationCd   = messages.StringField(1)                     #駅コード
    trainName   = messages.StringField(2)                     #路線名
    stationName   = messages.StringField(3)                   #駅名


class TrainMasterSrhStationListMsg(messages.Message):
    u"""駅リスト取得依頼メッセージ"""
    keyword = messages.StringField(1)              #検索ワード
                  
class TrainMasterSrhStationListResMsg(messages.Message):
    u"""駅リスト取得結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)
    stations = messages.MessageField(StationListItemMsg, 2, repeated=True)
