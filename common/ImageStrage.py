# coding: UTF-8
import cloudstorage as gcs
from kind.ImageKind import ImageKind 
from google.appengine.ext import ndb

class ImageStrage():
    u"""miral イメージ data Strage"""
    
    @classmethod
    def save(cls, filename_, imgData_, id_=0):

        with gcs.open(filename_, 'w') as f:
            f.write(imgData_)

            
        if id_ != 0:
            imageknd = ndb.Key("ImageKind", id_).get()
        else:    
            imageknd = ImageKind()
        
        imageknd.fileName = filename_;
        imageknd.put()
        
        return imageknd.key



            