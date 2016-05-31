# coding: UTF-8
from protorpc import messages
from google.appengine.ext import ndb

from common.msg.ApiResponceMsg import ApiResponceMsg
from kind.AccountKind import AccountKind
from code.LOGIN_TYPE import LOGIN_TYPE
from code.OK_NG import OK_NG
from code.UMU_FLG import UMU_FLG
from common.MiralLogger import MiralLogger
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralMsgTbl import MiralMsgTbl
from kind.SalonKind import SalonKind
from common.DateUtil import DateUtil
from common.service.AccountService import AccountService
from common.service.AccountService import AccountMsg

    
class SalonGalleyGetAllThumbnailMsg(messages.Message):
    u"""サロン ギャラリーの全てのサムネイオルを取得"""
    #salon = messages.MessageField(SalonAccountEditMsg, 1)          #サロン情報


class SalonGalleryAddImgMsg(messages.Message):
    u"""サロンアカウント新規登録結果メッセージ"""
    kindId = messages.StringField(1)                    #KindID
    order = messages.IntegerField(2)                    #順序
    imgbase64data = messages.StringField(3)             #イメージデータ

class SalonGalleryAddImgResMsg(messages.Message):
    u"""サロンアカウント新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    imgId = messages.StringField(2)                     #イメージID



