# coding: UTF-8
from common.MiralLogger import MiralLogger
import webapp2
from google.appengine.ext import ndb
import cloudstorage as gcs
import csv

from kind.master.MstTrainKind import MstTrainKind
class importTrainKind(webapp2.RequestHandler):

    #FILE_PATH = "/miral-1265.appspot.com/initdata/line20160402free.csv"
    FILE_PATH = "testdata/line20160402free.csv"
    
    def outDB(self):
        logger = MiralLogger()
        
        #データクリア
        ndb.delete_multi(
            MstTrainKind.query().fetch(keys_only=True)
        )        

        targetCampany = ("2","15","18")
        
        
        #with gcs.open(self.FILE_PATH, 'r') as f:
        with open(self.FILE_PATH, 'r') as f:
            reader = csv.reader(f,quotechar="'")
            
            next(reader)
            
            for row in reader:
                                
                train =  MstTrainKind();

                #テストではJR飲み
                if not row[1] in targetCampany :
                    continue
                
                train.trainCd=int(row[0])
                train.trainCompanyCd=int(row[1])
                train.trainName=row[2]
                train.trainNameKana=row[3]
                train.displayOrder=int(row[0])

                train.put()
        
        
    def get(self):
        self.outDB()
        self.response.out.write(u'終了!')
        