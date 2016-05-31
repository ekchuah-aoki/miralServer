# coding: UTF-8

from common.MiralLogger import MiralLogger
from common.ImageStrage import ImageStrage
from common.msg.ApiResponceMsg import ApiResponceMsg
from protorpc import messages
from code.OK_NG import OK_NG

from kind.master.MstTrainKind import MstTrainKind
from kind.master.MstStationKind import MstStationKind
from google.appengine.ext import ndb

from common.msg.ApiParamMsg import ApiParamMsg
from common.msg.TrainMasterMsg import TrainListItemMsg
from common.msg.TrainMasterMsg import TrainMasterGetTrainListResMsg 
from common.msg.TrainMasterMsg import StationListItemMsg 
from common.msg.TrainMasterMsg import TrainMasterSrhStationListResMsg 
    
class TrainRouteService():
    u"""沿線に関する処理"""


    def srhStationList(self, keyword_):
        logger = MiralLogger()
        
        qry = MstStationKind.query(ndb.AND(MstStationKind.stationName >= keyword_, MstStationKind.stationName <= keyword_ + u'\ufffd')) 

        results = qry.fetch()
        
        resMsg = TrainMasterSrhStationListResMsg()        
        resMsg.stations=[]

        for s in results:
            
            trainKind = s.trainKey.get()
            
            station = StationListItemMsg();
            station.stationCd = str(s.stationCd)
            station.stationName = s.stationName
            station.trainName = trainKind.trainName
        
            resMsg.stations.append(station)
            
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode()) 
        
        return resMsg    
            
    def getTrainList(self, reqMsg_):
        u"""路線情報を取得"""
        
        logger = MiralLogger()
        
        qry = MstTrainKind.query().order(MstTrainKind.displayOrder)
        
        if reqMsg_.pos == 1:
            results = qry.fetch(reqMsg_.limit)
        else:
            results = qry.fetch(reqMsg_.limit, offset=reqMsg_.pos-1)

        resMsg = TrainMasterGetTrainListResMsg()
        
        resMsg.trains=[]
        
        
        for t in results:
            
            #logger.debug(t.trainName)
            
            trainMsg = TrainListItemMsg()
            trainMsg.trainCd = t.trainCd
            trainMsg.trainName = t.trainName
        
            resMsg.trains.append(trainMsg)
            
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())    
        
        return resMsg

