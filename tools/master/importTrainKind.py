# coding: UTF-8
import webapp2
from kind.master.MstTrainKind import MstTrainKind

class importTrainKind(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        try:
            
            train =  MstTrainKind(
                            trainCd=1,
                            trainName='A'
                                  )
            train.put()
        except:
            self.response.out.write(u'異常終了!')
            return
                
        self.response.out.write(u'正常終了!')
        
        