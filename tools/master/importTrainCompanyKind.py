# coding: UTF-8
from common.MiralLogger import MiralLogger
import webapp2
from google.appengine.ext import ndb

from kind.master.MstTrainCompanyKind import MstTrainCampanyKind

class importTrainCompanyKind(webapp2.RequestHandler):
    
    data = [
        [2 , "JR東日本" , "ジェイアールヒガシニホン",2],
        [15 , "小田急電鉄" , "オダキュウデンテツ",15],
        [18 , "東京メトロ" , "トウキョウメトロ",18],
            ]
    
    def outDB(self):
        log = MiralLogger()
        
        #データクリア
        ndb.delete_multi(
            MstTrainCampanyKind.query().fetch(keys_only=True)
        )        
        
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
        