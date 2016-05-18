# coding: UTF-8

from code.CodeValue import CodeValue

class ACCOUNT_TYPE():
    u"""アカウント種別"""
    
    beauti =CodeValue(1, "美容師")
    salon =CodeValue(2, "サロン")
    
    @classmethod    
    def test(cls):
        return cls.__dict__
    
        
