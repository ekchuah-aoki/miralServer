# coding: UTF-8

from code.CodeValue import CodeValue
from code.CodeBase import CodeBase

class SALON_IMG_TYPE(CodeBase):
    u"""サロン　画像タイプ"""
    gallery =CodeValue(1, "gal")                 #ギャラリー画像大
    gallery_thumbnail=CodeValue(2, "galt")       #ギャラリー画像サムネール
    
    
    
