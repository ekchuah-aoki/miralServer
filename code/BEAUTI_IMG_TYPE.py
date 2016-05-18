# coding: UTF-8

from code.CodeValue import CodeValue
from code.CodeBase import CodeBase

class BEAUTI_IMG_TYPE(CodeBase):
    u"""美容師　画像タイプ"""
    laicense_original =CodeValue(1, "lcs01org")     #美容師免許原本画像
    laicense_thumbnail=CodeValue(2, "lcs01t")       #美容師免許サムネール
    
    
    
