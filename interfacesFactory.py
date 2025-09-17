#Contains all the abstract factory class

from abc import ABC, abstractmethod

class FurnitureFactory(ABC):
    
    @abstractmethod
    def createChair():
        pass

    @abstractmethod
    def createTable():
        pass
    
    @abstractmethod
    def createSofa():
        pass