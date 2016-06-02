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
from salon.msg.SalonGalleryServiceMsg import SalonGalleryAddImgResMsg
from common.MiralMsgTbl import MiralMsgTbl
from kind.SalonKind import SalonKind
from kind.SalonGalleryKind import SalonGalleryKind
from datetime import date
import time
from common.ImageUtil import ImageUtil
from salon.SalonImage import SalonImage
from code.SALON_IMG_TYPE import SALON_IMG_TYPE
from common.ImageStrage import ImageStrage

class SalonGalleryService():
    u"""サロン ギャラリーサービス"""
    
    _THUMBNAIL_W = 200
    _THUMBNAIL_H = 200
    
    _IMG_MAX_SIZE = 600
    

    @ndb.transactional(xg=True)            
    def add(self, salonId_, imgBase64Data_):

        salonKey = ndb.Key("SalonKind", long(salonId_)) 
        salonKind = salonKey.get()
        
        #Base64->バイナリ
        imgData = ImageUtil.base642blob(imgBase64Data_)
        
        #テスト
        thuImg = ImageUtil.crop(imgData, self._THUMBNAIL_W, self._THUMBNAIL_H)
        ImageStrage.testSave("test.jpg", thuImg)
        return
        
        #画像大
        daiImg = ImageUtil.resize(imgData, self._IMG_MAX_SIZE, self._IMG_MAX_SIZE)
        daiImgFileName = SalonImage.createImageFileName(salonId_, SALON_IMG_TYPE.gallery.getCode(), time.time() * 1000)
        daiBase64 =  ImageUtil.bolb2bse64(daiImg)
        daiImgKey = SalonImage.saveGalleryImage(salonId_, daiImgFileName, daiBase64)

        #サムネイル
        thuImg = ImageUtil.crop(imgData, self._THUMBNAIL_W, self._THUMBNAIL_H)
        thuImgFileName = SalonImage.createImageFileName(salonId_, SALON_IMG_TYPE.gallery_thumbnail.getCode(), time.time() * 1000)
        thuBase64 =  ImageUtil.bolb2bse64(thuImg)
        thuImgKey = SalonImage.saveGalleryImage(salonId_, thuImgFileName, thuBase64)
        
        if not salonKind.galleryKey:
            salonKind.galleryKey = [] 
        
        galleyKnd = SalonGalleryKind
        galleyKnd.imageKey = daiImgKey
        galleyKnd.thImageKey = thuImgKey
        galleyKnd.put()
        
        salonKind.galleryKey.append(galleyKnd)
        salonKind.put()
        
        resMsg = SalonGalleryAddImgResMsg()
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())
        resMsg.imgId = galleyKnd.key.id()
        resMsg.imgbase64data = thuBase64
        return resMsg
    
         
            