# coding: UTF-8
import logging

class MiralLogger(object):
    u"""miral ログユーティリティー"""
    
    __instance = None
    
    def __new__(cls, *a, **kw):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *a, **kw)


            cls.__instance.__logger = logging.getLogger("miralLogger")
            cls.__instance.__logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
            cls.__instance.__logger.addHandler(ch)

        return cls.__instance
    def debug(self,msg):
        self.__logger.debug(msg)
            
            
