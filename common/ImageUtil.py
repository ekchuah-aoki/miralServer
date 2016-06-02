# coding: UTF-8
from google.appengine.api import images
import base64
import math
from common.MiralLogger import MiralLogger

class ImageUtil():
    u"""miral ユーティリティー"""
    
    @classmethod
    def resize(cls, imageData_, maxH_, maxW_):
        img = images.Image(imageData_)
        
        resized = False
        
        if img.width > maxW_ or img.height > maxH_:
            
            if img.width > img.height:
                maxH_ = 0
            else:
                maxW_ = 0
                    
            img = images.resize(img, maxW_,maxH_)
            resized = True
                

        if resized:
            return img.execute_transforms(output_encoding=images.JPEG)
        else:
            return imageData_
    
    @classmethod
    def crop(cls, imageData_, maxH_, maxW_):
        
        img = images.Image(imageData_)
              
        img.resize(maxW_,maxH_, True)
         
        return img.execute_transforms(output_encoding=images.JPEG)

    @classmethod
    def bolb2bse64(cls, imgData_):
        return base64.b64encode(imgData_)
        
    @classmethod
    def base642blob(cls, imgBase64Data_):
        return base64.decodestring(imgBase64Data_)
