# coding: UTF-8
from common.MiralLogger import MiralLogger
from common.ImageStrage import ImageStrage
from code.SALON_IMG_TYPE import SALON_IMG_TYPE

class SalonImage(ImageStrage):
    
    IMAGE_PATH_ROOT = "/salon/"
    
    @classmethod
    def saveGalleryImage(cls, salonId_, fileName_, imgData_):
        
        fn =cls.getImageFileName(salonId_, fileName_)
        return cls.saveBase64(fn, imgData_)

            
    @classmethod
    def getImageFileName(cls, salonId_, fileName_):
        
        fileNameFmt = "{0}/{1}/{2}"
        return fileNameFmt.format(cls.IMAGE_PATH_ROOT, salonId_, fileName_)
    
    @classmethod
    def createImageFileName(cls, salonId_, type_, seq_):
        
        fileNameFmt = "{0}/{1}/{2}{3}.jpg"
        return fileNameFmt.format(cls.IMAGE_PATH_ROOT, salonId_, SALON_IMG_TYPE.getNameByCd(type_), str(seq_))
    
    @classmethod
    def getImageData(cls, salonId_, fileName_):

        fn =cls.getImageFileName(salonId_, fileName_)
        return cls.readBase64(fn)
        