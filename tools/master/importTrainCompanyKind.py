# coding: UTF-8
from common.MiralLogger import MiralLogger
import webapp2
from google.appengine.ext import ndb
import cloudstorage as gcs

from kind.master.MstTrainCompanyKind import MstTrainCampanyKind

class importTrainCompanyKind(webapp2.RequestHandler):

    #FILE_PATH = "/miral-1265.appspot.com"
    FILE_PATH = "/Users/y.aoki/myfolder/temp/company20160401-3.csv"
    
    def outDB(self):
        log = MiralLogger()
        
        #データクリア
        ndb.delete_multi(
            MstTrainCampanyKind.query().fetch(keys_only=True)
        )        

        #csvファイルオープン
        with gcs.open(self.FILE_PATH, 'r') as f:
            for row in self.data:
                
                train =  MstTrainCampanyKind(
                                campanyCd=row[0],
                                companyNama=row[1],
                                companyNameKana=row[2],
                                displayOrder=row[3]
                                      )
    
                train.put()
        
    def get(self):
        self.outDB()
        self.response.out.write(u'終了!')
        