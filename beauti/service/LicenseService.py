# coding: UTF-8

from beauti.BeautiImage import BeautiImage
from common.ImageUtil import ImageUtil
from google.appengine.ext import ndb
from kind.BeauticianLicenseKind import BeauticianLicenseKind
from code.OK_NG import OK_NG
from code.UMU_FLG import UMU_FLG
from code.BEAUTI_IMG_TYPE import BEAUTI_IMG_TYPE
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralLogger import MiralLogger
from protorpc import messages

from beauti.msg.LicenseServiceMsg import LicenseAddMsg
from beauti.msg.LicenseServiceMsg import LicenseAddResMsg
from beauti.msg.LicenseServiceMsg  import LicenseGetThumbnailImgResMsg


class LicenseService():

    _THUMBNAIL_W = 100
    _THUMBNAIL_H = 200    
    def set(self, beautiId_, imgBase64Data_):

        beautiKey = ndb.Key("BeauticianKind", long(beautiId_)) 
        beautiKind = beautiKey.get()
        
        if beautiKind.licenseKey:
            
            #すでに登録ずみ
            licenseKnd = beautiKind.licenseKey.get()
            
            #既存データ消去
            BeautiImage.deleteKind(licenseKnd.imageKey)
            BeautiImage.deleteKind(licenseKnd.thImageKey)
            
        else:    
            licenseKnd = BeauticianLicenseKind()
        
        imgData = ImageUtil.base642blob(imgBase64Data_)

        #原本画像登録
        orignKey = BeautiImage.saveLicenseImage(beautiId_, BEAUTI_IMG_TYPE.laicense_original.getCode(), imgData)
        
        #現行サイズ画像登録
        #orignKey = BeautiImage.saveLicenseImage(beautiId_, BeautiImage.IMGTYPE_LAICENSE_IMAGE, imgBase64Data_)
        
        #サムネイル登録
        thImage = ImageUtil.resize(imgData, self._THUMBNAIL_W, self._THUMBNAIL_H)
        thBase64 =  ImageUtil.bolb2bse64(thImage)
        thumKey = BeautiImage.saveLicenseImage(beautiId_, BEAUTI_IMG_TYPE.laicense_thumbnail.getCode(), thBase64)
            
        licenseKnd.imageKey = orignKey
        licenseKnd.thImageKey = thumKey
        licenseKnd.put()
        
        if not beautiKind.licenseKey:
            beautiKind.licenseKey = licenseKnd.key
            beautiKind.put()
        
        resMsg = LicenseAddResMsg()
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        return resMsg
       
    def getThumbnailImage(self, beautiId_):
        
        resMsg = LicenseGetThumbnailImgResMsg()
        
        base64Data = BeautiImage.getImageData(beautiId_, BEAUTI_IMG_TYPE.laicense_thumbnail.getCode())
            
        if not base64Data:
            resMsg.res = ApiResponceMsg(rstCode=UMU_FLG.nasi.getCode())
        else:
            resMsg.res = ApiResponceMsg(rstCode=UMU_FLG.ari.getCode())
            resMsg.imgbase64data = base64Data

        return resMsg

        
        