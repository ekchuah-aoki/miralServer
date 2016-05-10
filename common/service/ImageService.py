# coding: UTF-8

from common.MiralLogger import MiralLogger
from common.ImageStrage import ImageStrage
from common.msg.ApiResponceMsg import ApiResponceMsg
from protorpc import messages
from code.OK_NG import OK_NG


class ImageGetMsg(messages.Message):
    u"""画像データ取得依頼メッセージ"""
    fileName  = messages.StringField(1)                 #イメージファイル名
    
class ImageGetResMsg(messages.Message):
    u"""画像データ取得結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)
    imgBase64Data = messages.StringField(2)     
    
class ImageService():
    u"""イメージ処理"""

    def load(self, fileName_):
        
        resMsg = ImageGetResMsg();
        
        resMsg.imgBase64Data = ImageStrage.readBase64(fileName_)
        
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())        
        
        return resMsg
