# coding: UTF-8

from common.MiralLogger import MiralLogger
from common.ImageStrage import ImageStrage
from common.msg.ApiResponceMsg import ApiResponceMsg
from protorpc import messages
from code.OK_NG import OK_NG

from kind.master.MstTrainKind import MstTrainKind

from common.msg.ApiParamMsg import ApiParamMsg
from common.msg.TrainMasterMsg import TrainListItemMsg
from common.msg.TrainMasterMsg import TrainMasterGetTrainListResMsg 
    
class TrainRouteService():
    u"""沿線に関する処理"""

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

