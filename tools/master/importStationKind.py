# coding: UTF-8
from common.MiralLogger import MiralLogger
import webapp2
from google.appengine.ext import ndb
import cloudstorage as gcs
import csv
from kind.master.MstStationKind import MstStationKind
from kind.master.MstTrainKind import MstTrainKind

class importStationKind(webapp2.RequestHandler):

    #FILE_PATH = "/miral-1265.appspot.com/initdata/station20160401free.csv"
    FILE_PATH = "testdata/station20160401free.csv"
    
    def outDB(self, delflg):
        log = MiralLogger()
        
        #データクリア
        if delflg:
            log.debug("delete!!!!!!!!!!")
            ndb.delete_multi(
                MstStationKind.query().fetch(keys_only=True)
            )    
            
            return 0
            
        #with gcs.open(self.FILE_PATH, 'r') as f:
        with open(self.FILE_PATH, 'r') as f:
            reader = csv.reader(f,quotechar="'")
            
            next(reader)
            
            for c in range(MstStationKind().query().count()):
                next(reader)
                
            #ターゲット路線
            targetTrainList=[]
            targetTrainKeyList={}
            
            qry = MstTrainKind.query()
            
            for tr in qry.fetch():
                targetTrainList.append(str(tr.trainCd))
                targetTrainKeyList[str(tr.trainCd)]=tr.key
            
            c2=0
            
            for row in reader:
                
                if not row[5] in targetTrainList:
                    continue


                station = MstStationKind()
                
                station.stationCd=int(row[0])
                station.stationGpCd=int(row[1])
                station.stationName=row[2]
                station.trainKey=targetTrainKeyList[row[5]]
                station.geoCd=ndb.GeoPt(float(row[10]),float(row[9]))
                station.displayOrder=int(row[1])

                station.put()
                
                c2=c2+1
                 
                if c2 > 1000:
                    break
            
            return c2
        
    def getCount(self):
        return MstStationKind().query().count()
        
    def get(self):
        
        d = self.request.GET['delete']
        
        if d=="1":
            c = self.outDB(d)
        else:
            c = self.outDB(False)
            
        self.response.out.write(u'終了! ' + str(c) + " "+str(MstStationKind().query().count()))
        