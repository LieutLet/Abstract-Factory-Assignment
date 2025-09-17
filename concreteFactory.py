from interfacesFactory import *
from concreteFurniture import *

class ModernFurnitureFactory(FurnitureFactory):
    def __init__(self):
        self.style = "Modern"
    
    def createChair():
        return ModernChair()
        

class VictorianFurnitureFactory(FurnitureFactory):
    def __init__(self):
        self.style = "Victorian"
    
    def createChair():
        return VictorianChair()

class ArtDecoFurnitureFactory(FurnitureFactory):
    def __init__(self):
        self.style = "ArtDeco"
    
    def createChair():
        return ArtDecoChair()