from interfacesFurniture import *

class ModernChair(IChair):
    def __init__(self):
        self.style = "Modern"
        self.material = "Steel and Leather"
        self.price = 299.99
    
    def sitOn(self):
        return f"You are sitting on a {self.style} chair."
    
    def get_description(self):
        return f"{self.style} Chair - Material: {self.material}, Price: ${self.price}"
    
class VictorianChair(IChair):
    def __init__(self):
        self.style = "Victorian"
        self.material = "Mahogany"
        self.price = 499.99
    
    def sitOn(self):
        return f"You are sitting on a {self.style} chair."
    
    def get_description(self):
        return f"{self.style} Chair - Material: {self.material}, Price: ${self.price}"

class ArtDecoChair(IChair):
    def __init__(self):
        self.style = "Art Deco"
        self.material = "Walnut"
        self.price = 399.99
    
    def sitOn(self):
        return f"You are sitting on a {self.style} chair."
    
    def get_description(self):
        return f"{self.style} Chair - Material: {self.material}, Price: ${self.price}"
    
class ModernTable(ITable):
    def __init__(self):
        self.style = "Modern"
        self.material = "Glass and Chrome"
        self.price = 599.99
    
    def placeItems(self):
        return f"You placed items on a {self.style} table."
    
    def get_description(self):
        return f"{self.style} Table - Material: {self.material}, Price: ${self.price}"

class VictorianTable(ITable):
    def __init__(self):
        self.style = "Victorian"
        self.material = "Oak"
        self.price = 799.99
    
    def placeItems(self):
        return f"You placed items on a {self.style} table."
    
    def get_description(self):
        return f"{self.style} Table - Material: {self.material}, Price: ${self.price}"

class ArtDecoTable(ITable):
    def __init__(self):
        self.style = "Art Deco"
        self.material = "Marble and Brass"
        self.price = 999.99
    
    def placeItems(self):
        return f"You placed items on a {self.style} table."
    
    def get_description(self):
        return f"{self.style} Table - Material: {self.material}, Price: ${self.price}"

class ModernSofa(ISofa):
    def __init__(self):
        self.style = "Modern"
        self.material = "Microfiber"
        self.price = 899.99
    
    def relaxOn(self):
        return f"You are relaxing on a {self.style} sofa."
    
    def get_description(self):
        return f"{self.style} Sofa - Material: {self.material}, Price: ${self.price}"

class VictorianSofa(ISofa):
    def __init__(self):
        self.style = "Victorian"
        self.material = "Velvet"
        self.price = 1299.99
    
    def relaxOn(self):
        return f"You are relaxing on a {self.style} sofa."
    
    def get_description(self):
        return f"{self.style} Sofa - Material: {self.material}, Price: ${self.price}"

class ArtDecoSofa(ISofa):
    def __init__(self):
        self.style = "Art Deco"
        self.material = "Silk"
        self.price = 1599.99
    
    def relaxOn(self):
        return f"You are relaxing on a {self.style} sofa."
    
    def get_description(self):
        return f"{self.style} Sofa - Material: {self.material}, Price: ${self.price}"