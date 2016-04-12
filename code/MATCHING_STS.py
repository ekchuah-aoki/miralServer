# coding: UTF-8

from code.CodeValue import CodeValue

class MATCHING_STS():
    u"""マッチングステータス"""
    
    request =CodeValue(1, "依頼中")
    matching =CodeValue(2, "マッチング")
    refuse =CodeValue(3, "拒否")
    end =CodeValue(4, "終了")
    
    
