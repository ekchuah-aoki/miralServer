# coding: UTF-8
from datetime import time
from datetime import date
from common.MiralLogger import MiralLogger

class DateUtil():
    u"""日時ユーティリティー"""
    
    @classmethod
    def getTimeByStr(cls, strTime_):
        
        h = strTime_[0:2]
        m = strTime_[2:4]
        
        if len(strTime_)<=4:
            s = "0"
        else:
            s = strTime_[4:]
        
        logger = MiralLogger()
        
        logger.debug(str(len(strTime_))+","+h+","+m+","+s)
        
        return time(int(h), int(m), int(s))

    @classmethod
    def getDateByStr(cls, yyyy, mm, dd):
        return date(int(yyyy), int(mm),int(dd))   
    
    @classmethod
    def splitStrTime(cls,time_):
        
        if not time_:
            return  {"hour":"", "minute":"", "second":""}
        
        h = str(time_.hour);
        
        m = str(time_.minute)
        if time_.minute < 9:
            m = "0" + m
 
        s = str(time_.second)
        if time_.second < 9:
            s = "0" + s
            
        return {"hour":h, "minute":m, "second":s}

                