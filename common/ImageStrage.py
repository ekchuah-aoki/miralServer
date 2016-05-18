# coding: UTF-8
import cloudstorage as gcs
from kind.ImageKind import ImageKind 
from google.appengine.ext import ndb
from common.MiralLogger import MiralLogger

class ImageStrage():
 
    u"""miral イメージ data Strage"""
 
    IMAGE_BASE_PATH = "/miral-1265.appspot.com"
 
    
    @classmethod
    def save(cls, filename_, imgData_, id_=0):
        
        logger = MiralLogger() 
        logger.debug("ImageStrage save:"+filename_)
        
        with gcs.open(cls.IMAGE_BASE_PATH + filename_, 'w') as f:
            f.write(imgData_)

        return cls.saveKind(filename_, id_)


    @classmethod
    def saveBase64(cls, filename_, imgBase64Data_, id_=0):
        
        logger = MiralLogger() 
        logger.debug("ImageStrage saveBase64:"+filename_)
        
        with gcs.open(cls.IMAGE_BASE_PATH + filename_, "w") as f:
            f.write(imgBase64Data_.encode('utf-8'))
        
        
        return cls.saveKind(filename_, id_)

    
    @classmethod
    def saveKind(cls, filename_, id_):
        if id_ != 0:
            imageknd = ndb.Key("ImageKind", id_).get()
        else:    
            imageknd = ImageKind()
        
        imageknd.fileName = filename_;
        imageknd.put()
        
        return imageknd.key
        
    @classmethod
    def read(cls, filename_):
        with gcs.open(cls.IMAGE_BASE_PATH + filename_, 'r') as f:
            return f.read()


    @classmethod
    def readBase64(cls, filename_):
        with gcs.open(cls.IMAGE_BASE_PATH + filename_, "r") as f:
            data = f.read().decode('utf-8')
        
        return data
        
    @classmethod
    def deleteKind(cls, key_):
        key_.delete()
        