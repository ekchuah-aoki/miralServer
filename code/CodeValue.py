# coding: UTF-8
class CodeValue():
    u"""コード値"""
    def __init__(self, c_, n_):
        self.__code = c_
        self.__name = n_

    def getCode(self):
        return self.__code
    
    def getName(self):
        return self.__name
    
    def equalCd(self, code_):
        if self.__code == code_:
            return True
        else:
            return False
