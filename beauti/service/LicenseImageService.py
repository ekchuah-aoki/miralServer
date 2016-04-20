# coding: UTF-8
import base64
from beauti.BeautiImage import BeautiImage
from common.ImageUtil import ImageUtil
from google.appengine.ext import ndb
from kind.BeauticianLicenseKind import BeauticianLicenseKind
from code.OK_NG import OK_NG
from common.msg.ApiResponceMsg import ApiResponceMsg
from beauti.msg.BeautiImageResMsg import BeautiImageResMsg
from common.MiralLogger import MiralLogger

class LicenseImageService():

    _THUMBNAIL_W = 100
    _THUMBNAIL_H = 200    
    def add(self, accountId_, imgBase64Data_):

                
        imgData = base64.decodestring(imgBase64Data_)
        
        #原本画像登録
        orignKey = BeautiImage.saveLicenseImage(accountId_, BeautiImage.IMGTYPE_LAICENSE_IMAGE, imgData)
        
        #サムネイル登録
        thImage = ImageUtil.resize(imgData, self._THUMBNAIL_W, self._THUMBNAIL_H) 
        thumKey = BeautiImage.saveLicenseImage(accountId_, BeautiImage.IMGTYPE_LAICENSE_THUMBNAIL_IMAGE, thImage)
        
       
        
        accKey = ndb.Key("AccountKind", long(accountId_)) 
        
        licenseKnd = BeauticianLicenseKind()
        licenseKnd.accountKey = accKey
        licenseKnd.imageData = orignKey
        licenseKnd.thImageData = thumKey
        licenseKnd.put()
 
        resMsg = BeautiImageResMsg()
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        return resMsg
       
        
        
        