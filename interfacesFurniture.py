#Contains all the abstract classes to make furniture

from abc import ABC, abstractmethod
#all chair styles inherit from IChair
class IChair(ABC):
    """Basic chair class - new implementation"""
    
    def __init__(self, style: str, material: str, price: float):
        self.style = style
        self.material = material
        self.price = price
    
    def sit_on(self):
        print(f"Sitting on a {self.style} chair made of {self.material}")
    
    def get_description(self) -> str:
        return f"{self.style} chair made of {self.material} - ${self.price}"
    
#all table styles inherit from ITable
class ITable(ABC):
    """Basic table class - new implementation"""
    
    def __init__(self, style: str, material: str, price: float):
        self.style = style
        self.material = material
        self.price = price
    
    def place_items(self):
        print(f"Placing items on a {self.style} table made of {self.material}")
    
    def get_description(self) -> str:
        return f"{self.style} table made of {self.material} - ${self.price}"

#all sofa styles inherit from ISofa
class ISofa(ABC):
    """Basic sofa class - new implementation"""
    
    def __init__(self, style: str, material: str, price: float):
        self.style = style
        self.material = material
        self.price = price
    
    def relax_on(self):
        print(f"Relaxing on a {self.style} sofa made of {self.material}")
    
    def get_description(self) -> str:
        return f"{self.style} sofa made of {self.material} - ${self.price}"