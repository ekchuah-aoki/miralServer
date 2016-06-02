# coding: UTF-8
from protorpc import messages
from google.appengine.ext import ndb

from common.msg.ApiResponceMsg import ApiResponceMsg
from kind.AccountKind import AccountKind
from code.LOGIN_TYPE import LOGIN_TYPE
from code.OK_NG import OK_NG
from code.UMU_FLG import UMU_FLG
from code.SALON_LIST_ORDER_COL import SALON_LIST_ORDER_COL
from common.MiralLogger import MiralLogger
from common.msg.ApiResponceMsg import ApiResponceMsg
from common.MiralMsgTbl import MiralMsgTbl
from kind.SalonKind import SalonKind
from datetime import date
from salon.msg.SalonQueryServiceMsg import SalonSearchByKeywordResMsg
from salon.msg.SalonQueryServiceMsg import SalonSrhItemMsg
from common.service.TrainMastrService import TrainRouteService

class SalonQueryService():
    u"""サロンクエリーサービス"""
    
    def searchByKeyword(self, reqMsg_):
        
        keyword = reqMsg_.keyword
        
        logger = MiralLogger()

        resMsg = SalonSearchByKeywordResMsg()
        
        qry = SalonKind.query()
        

        logger 
        
        #ポジションが1の時は検索対象件数を取得
        if reqMsg_.pos == 1:
            resMsg.count = qry.count()  
        
        #並び替え項目
        if not reqMsg_.orderCol:
            reqMsg_.orderCol = SALON_LIST_ORDER_COL.NameKana.getCode()
        
        
        if reqMsg_.orderCol == SALON_LIST_ORDER_COL.NameKana.getCode():
            orderCol = SalonKind.nameKana
        
        qry = qry.order(orderCol)
        
        
        if reqMsg_.pos == 1:
            results = qry.fetch(reqMsg_.limit)
        else:
            results = qry.fetch(reqMsg_.limit, offset=reqMsg_.pos-1)

        
        resMsg.salons=[]
        
        trainService = TrainRouteService()
        
        for s in results:
            
            #logger.debug(t.trainName)
            
            
            
            salon = SalonSrhItemMsg()
            salon.oneHourPoint= s.oneHourPoint                #一時間利用ポイント
            salon.oneDayPoint= s.oneDayPoint                 #一日利用ポイント
            salon.compEval= s.compEval              #検索対象最低総合評価

            if s.stationKey:
                stationName = trainService.getStationNameByKey(s.stationKey)
                salon.stationName= stationName["trainName"] + " " + stationName["stationName"]                 #最寄り駅
                
            salon.workingTime= s.workingTime                     #駅徒歩
            salon.name= s.name                         #店舗名
            salon.mainImgFileName= None              #メイン画像ファイル名
            
        
            resMsg.salons.append(salon)
            
        resMsg.res = ApiResponceMsg(rstCode=OK_NG.ok.getCode())    
        
        return resMsg

            