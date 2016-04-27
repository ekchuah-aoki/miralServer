# coding: UTF-8
from datetime import time
from datetime import date

class DateUtil():
    u"""日時ユーティリティー"""
    
    @classmethod
    def getTimeByStr(cls, strTime_):
        
        h = strTime_[0,2]
        m = strTime_[1,2]
        s = strTime_[3,2]
        
        return time.struct_time(tm_hour=h, tm_min=m, tm_sec=s)

    @classmethod
    def getDateByStr(cls, yyyy, mm, dd):
        return date(int(yyyy), int(mm),int(dd))    