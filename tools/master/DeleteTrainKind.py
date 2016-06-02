# coding: UTF-8
from common.MiralLogger import MiralLogger
import webapp2
from google.appengine.ext import ndb
import cloudstorage as gcs
import csv

from kind.master.MstTrainKind import MstTrainKind
from kind.master.MstStationKind import MstStationKind

class DeleteTrainKind(webapp2.RequestHandler):

    FILE_PATH = "/miral-1265.appspot.com/initdata/line20160402free.csv"
    #FILE_PATH = "testdata/line20160402free.csv"
    
    def outDB(self):
        logger = MiralLogger()
        

        #targetCampany = (2)
        
        qry = MstTrainKind.query(MstTrainKind.trainCd != 2)
        
        trains = qry.fetch(keys_only=True)
        
        for t in trains:
            ndb.delete_multi(
                MstStationKind.query(MstStationKind.trainKey == t).fetch(keys_only=True)
            )        
            
        
        #データクリア
        qry = MstTrainKind.query(MstTrainKind.trainCd != 2)
        ndb.delete_multi(
            qry.fetch(keys_only=True)
        )        
        
        
        
    def get(self):
        self.outDB()
        self.response.out.write(u'終了!')
        