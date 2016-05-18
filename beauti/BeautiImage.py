# coding: UTF-8
from common.MiralLogger import MiralLogger
from common.ImageStrage import ImageStrage
from code.BEAUTI_IMG_TYPE import BEAUTI_IMG_TYPE

class BeautiImage(ImageStrage):
    
    #IMAGE_PATH = "/beauti/"
    IMAGE_PATH = "/beauti/{0}/{1}.jpg"
    #IMGTYPE_LAICENSE_IMAGE_ORIGINAL = "lcs01org"
    #IMGTYPE_LAICENSE_IMAGE = "lcs01"
    #IMGTYPE_LAICENSE_THUMBNAIL_IMAGE = "lcs01t"
    
    @classmethod
    def saveLicenseImage(cls, beautiId_, type_, imgData_):
        
        fn =cls.getImageFileName(beautiId_, type_)
        
        if type_ == BEAUTI_IMG_TYPE.laicense_original.getCode():
            return cls.save(fn, imgData_)
        else:
            
            return cls.saveBase64(fn, imgData_)

            
    @classmethod
    def getImageFileName(cls, beautiId_, type_):
        
        fn = cls.IMAGE_PATH.format(beautiId_, BEAUTI_IMG_TYPE.getNameByCd(type_))
        
        return fn
    
    
    @classmethod
    def getImageData(cls, beautiId_, type_):

        fn =cls.getImageFileName(beautiId_, type_)

        #美容師免許意外はbase64形式で保存されている
        if type_ == BEAUTI_IMG_TYPE.laicense_original.getCode():
            return cls.read(fn)
        else:
            return cls.readBase64(fn)
        