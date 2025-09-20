# concrete factories for different furniture styles, each class inherits from FurnitureFactory
# and implements methods to create chairs, tables, and sofas of that style, each method just returns
# an instance of the corresponding concrete furniture class

from interfacesFactory import *
from concreteFurniture import *

class ModernFurnitureFactory(FurnitureFactory):
    def __init__(self):
        self.style = "Modern"
    
    def createChair(self):
        return ModernChair()
    
    def createTable(self):
        return ModernTable()
    
    def createSofa(self):
        return ModernSofa()
        

class VictorianFurnitureFactory(FurnitureFactory):
    def __init__(self):
        self.style = "Victorian"
    
    def createChair(self):
        return VictorianChair()
    
    def createTable(self):
        return VictorianTable()
    
    def createSofa(self):
        return VictorianSofa()
    

class ArtDecoFurnitureFactory(FurnitureFactory):
    def __init__(self):
        self.style = "ArtDeco"
    
    def createChair(self):
        return ArtDecoChair()
    
    def createTable(self):
        return ArtDecoTable()
    
    def createSofa(self):
        return ArtDecoSofa()
    