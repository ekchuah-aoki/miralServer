# coding: UTF-8

from beauti.BeautiImage import BeautiImage
from common.ImageUtil import ImageUtil
from google.appengine.ext import ndb
from kind.BeauticianLicenseKind import BeauticianLicenseKind
from code.OK_NG import OK_NG
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralLogger import MiralLogger
from protorpc import messages

class LicenseAddMsg(messages.Message):
    u"""美容師の美容師免許の新規登録依頼メッセージ"""
    beautiId = messages.StringField(1)                   #美容師ID
    imgbase64data = messages.StringField(2)              #イメージデータ

class LicenseAddResMsg(messages.Message):
    u"""美容師の美容師免許の新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果


class LicenseGetThumbnailImgMsg(messages.Message):
    u"""美容師の美容師免許の画像取得メッセージ"""
    beautiId = messages.StringField(1)                   #美容師ID
    
class LicenseGetThumbnailImgResMsg(messages.Message):
    u"""美容師の美容師免許の画像取得結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果
    imgbase64data = messages.StringField(2)              #イメージデータ
    