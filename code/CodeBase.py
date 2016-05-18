# coding: UTF-8

from code.CodeValue import CodeValue
from common.MiralLogger import MiralLogger

class CodeBase():

    @classmethod    
    def getNameByCd(cls, cd):

        logger = MiralLogger()
        
        logger.debug("CodeBase.getNameByCd   "+str(cd))

                
        for k, v in cls.__dict__.items():
            
            logger.debug(k)
            if isinstance(v, CodeValue):
                logger.debug("aaaaaaaaaaaaaaaaaaa" +str(v.getCode()))
                if v.getCode()==cd:
                    logger.debug("bbbbbbbbbbbbbbbbbbbbbbbbbbb")
                    return v.getName()
                
            
        return None
    

