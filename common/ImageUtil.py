# coding: UTF-8
from google.appengine.api import images

class ImageUtil():
    u"""miral ユーティリティー"""
    
    @classmethod
    def resize(cls, imageData_, maxH_, maxW_):
        img = images.Image(imageData_)
        
        resized = False
        
        if img.width > img.height or img.height > maxH_:
            img.resize(maxW_,maxH_)
            resized = True
                

        if resized:
            return img.execute_transforms(output_encoding=images.JPEG)
        else:
            return imageData_
