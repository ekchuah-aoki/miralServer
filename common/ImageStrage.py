# coding: UTF-8
import cloudstorage as gcs
from kind.ImageKind import ImageKind 
from google.appengine.ext import ndb
from common.MiralLogger import MiralLogger
from google.appengine.tools.devappserver2.python.stubs import FakeFile
class ImageStrage():
 
    u"""miral イメージ data Strage"""
 
    IMAGE_BASE_PATH = "/miral-1265.appspot.com"
    TEST_IMAGE_BASE_PATH = "testdata/"
 
    @classmethod
    def testSave(cls, filename_, imgData_):
        allowed_modes = FakeFile.ALLOWED_MODES
        FakeFile.ALLOWED_MODES = frozenset(['wb'])        
        FakeFile.set_allowed_paths("/Users/y.aoki/myfolder/project/miral/src/miralServer", ["testdata"])

        logger = MiralLogger() 
        logger.debug("ImageStrage testSave:"+filename_)
        
        with open(cls.TEST_IMAGE_BASE_PATH + filename_, 'wb') as f:
            f.write(imgData_)
            
        FakeFile.ALLOWED_MODES = allowed_modes    
           
    @classmethod
    def testRead(cls, filename_):
        logger = MiralLogger() 
        logger.debug("ImageStrage testRead:"+cls.TEST_IMAGE_BASE_PATH + filename_)
        with open(cls.TEST_IMAGE_BASE_PATH + filename_, 'rb') as f:
            return f.read()
       
        
    @classmethod
    def save(cls, filename_, imgData_, id_=0):
        
        logger = MiralLogger() 
        logger.debug("ImageStrage save:"+filename_)
        
        with gcs.open(cls.IMAGE_BASE_PATH + filename_, 'wb') as f:
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
        try:
            with gcs.open(cls.IMAGE_BASE_PATH + filename_, 'rb') as f:
                return f.read()
        except:
            return None    

    @classmethod
    def readBase64(cls, filename_):
        try:
            with gcs.open(cls.IMAGE_BASE_PATH + filename_, "r") as f:
                data = f.read().decode('utf-8')
            
            return data
        except:
            return None    
        
    @classmethod
    def deleteKind(cls, key_):
        key_.delete()
        