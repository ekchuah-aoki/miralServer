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
    u"""アカウント新規登録依頼メッセージ"""
    accountId = messages.StringField(1)                 #アカウントID
    imgbase64data = messages.StringField(2)              #イメージデータ

class LicenseAddResMsg(messages.Message):
    u"""アカウント新規登録結果メッセージ"""
    res = messages.MessageField(ApiResponceMsg, 1)      #結果


class LicenseService():

    _THUMBNAIL_W = 100
    _THUMBNAIL_H = 200    
    def add(self, accountId_, imgBase64Data_):

                
        imgData = ImageUtil.base642blob(imgBase64Data_)
        
        #原本画像登録
        BeautiImage.saveLicenseImage(accountId_, BeautiImage.IMGTYPE_LAICENSE_IMAGE_ORIGINAL, imgData)
        orignKey = BeautiImage.saveLicenseImage(accountId_, BeautiImage.IMGTYPE_LAICENSE_IMAGE, imgBase64Data_)
        
        #サムネイル登録
        thImage = ImageUtil.resize(imgData, self._THUMBNAIL_W, self._THUMBNAIL_H)
        thBase64 =  ImageUtil.bolb2bse64(thImage)
        thumKey = BeautiImage.saveLicenseImage(accountId_, BeautiImage.IMGTYPE_LAICENSE_THUMBNAIL_IMAGE, thBase64)
        
        accKey = ndb.Key("BeauticianKind", long(accountId_)) 
        
        licenseKnd = BeauticianLicenseKind()
        licenseKnd.beautiKey = accKey
        licenseKnd.imageKey = orignKey
        licenseKnd.thImageKey = thumKey
        licenseKnd.put()
        
        resMsg = LicenseAddResMsg()
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        return resMsg
       
    def getThumbnailImage(self, accountId_, type_):
        return BeautiImage.getImageData(accountId_, type_)
            
        
        