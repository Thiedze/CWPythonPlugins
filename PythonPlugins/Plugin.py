import abc

class Plugin():
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self):
        pass
    
    @abc.abstractmethod
    def setCallback(self, callbackFunction):
        pass     
    
    @abc.abstractmethod
    def prepare(self, Text):
        pass 