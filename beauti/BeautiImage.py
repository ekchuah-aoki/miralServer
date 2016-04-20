# coding: UTF-8
from common.MiralLogger import MiralLogger
from common.ImageStrage import ImageStrage

class BeautiImage(ImageStrage):
    
    #IMAGE_PATH = "/beauti/"
    IMAGE_PATH = "/miral-1265.appspot.com/beauti/{0}/{1}.jpg"
    IMGTYPE_LAICENSE_IMAGE = "l01"
    IMGTYPE_LAICENSE_THUMBNAIL_IMAGE = "l01t"
    
    @classmethod
    def saveLicenseImage(cls, userId_, type_, imgData_):
        
         
        fn = cls.IMAGE_PATH.format(userId_, type_)
        
        
        return cls.save(fn, imgData_)

            
