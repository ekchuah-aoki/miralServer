# coding: UTF-8
from common.MiralLogger import MiralLogger
from common.ImageStrage import ImageStrage

class BeautiImage(ImageStrage):
    
    #IMAGE_PATH = "/beauti/"
    IMAGE_PATH = "/salon/{0}/{1}.jpg"
    IMGTYPE_OWNER_IMAGE = "owr01"       #オーナー画像のサイズは一種類のみ
    
    @classmethod
    def saveLicenseImage(cls, accountId_, type_, imgData_):
        
        fn =cls.getImageFileName(accountId_, type_)
        
        if type_ == cls.IMGTYPE_LAICENSE_IMAGE_ORIGINAL:

            return cls.save(fn, imgData_)
        else:
            
            return cls.saveBase64(fn, imgData_)

            
    @classmethod
    def getImageFileName(cls, accountId_, type_):
        
        fn = cls.IMAGE_PATH.format(accountId_, type_)
        
        return fn
    
    
    @classmethod
    def getImageData(cls, accountId_, type_):

        fn =cls.getImageFileName(accountId_, type_)

        if type_ == cls.IMGTYPE_LAICENSE_IMAGE_ORIGINAL:

            return cls.read(fn)
        else:
            return cls.readBase64(fn)
        