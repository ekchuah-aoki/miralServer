# coding: UTF-8
from common.MiralLogger import MiralLogger
import webapp2
from google.appengine.ext import ndb
import cloudstorage as gcs
import csv
from common.ImageUtil import ImageUtil 
from common.ImageStrage import ImageStrage


from kind.master.MstTrainKind import MstTrainKind
class imageSample1(webapp2.RequestHandler):

    def crop(self):
        logger = MiralLogger()
        
        logger.debug("★★★★★★ image read")
        img = ImageStrage.testRead("img1.jpg")
        
        if not img:
            logger.debug("★★★★★★ !!!!!!!!!!!!!!!!!!!!")
            
        
        img = ImageUtil.crop(img, 200, 200)
        
        ImageStrage.testSave("img2.jpg", img)
        
        
    def get(self):
        self.crop()
        self.response.out.write(u'終了!  ' )
        