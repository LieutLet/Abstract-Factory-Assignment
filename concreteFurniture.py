from interfacesFurniture import *

# Concrete implementations of chairs, tables, and sofas for different styles
# each class now holds its own style, material, and price attributes instead of passing them during instantiation

# Though not necessary, I added getter methods for material and price in the concrete products as an example 
# of how to extend functionality

#==================================================================================================================#
#Chair Implementations
#==================================================================================================================#

class ModernChair(IChair):
    def __init__(self):
        self.style = "Modern"
        self.material = "Steel and Leather"
        self.price = 299.99
    
    def sitOn(self):
        return f"You are sitting on a {self.style} chair."
    
    def get_description(self):
        return f"{self.style} Chair - Material: {self.material}, Price: ${self.price}"
    
    def sit_on(self):
        return f"You are sitting on a {self.style} chair."

    def get_material(self):
        return self.material

    def get_price(self):
        return self.price
    
    
class VictorianChair(IChair):
    def __init__(self):
        self.style = "Victorian"
        self.material = "Mahogany"
        self.price = 499.99
    
    def sit_on(self):
        return f"You are sitting on a {self.style} chair."
    
    def get_description(self):
        return f"{self.style} Chair - Material: {self.material}, Price: ${self.price}"

class ArtDecoChair(IChair):
    def __init__(self):
        self.style = "Art Deco"
        self.material = "Walnut"
        self.price = 399.99
    
    def sit_on(self):
        return f"You are sitting on a {self.style} chair."
    
    def get_description(self):
        return f"{self.style} Chair - Material: {self.material}, Price: ${self.price}"
    

#==================================================================================================================#
#Table Implementations
#==================================================================================================================#
class ModernTable(ITable):
    def __init__(self):
        self.style = "Modern"
        self.material = "Glass and Chrome"
        self.price = 599.99
    
    def place_items(self):
        return f"You placed items on a {self.style} table."
    
    def get_description(self):
        return f"{self.style} Table - Material: {self.material}, Price: ${self.price}"

class VictorianTable(ITable):
    def __init__(self):
        self.style = "Victorian"
        self.material = "Oak"
        self.price = 799.99
    
    def place_items(self):
        return f"You placed items on a {self.style} table."
    
    def get_description(self):
        return f"{self.style} Table - Material: {self.material}, Price: ${self.price}"


class ArtDecoTable(ITable):
    def __init__(self):
        self.style = "Art Deco"
        self.material = "Marble and Brass"
        self.price = 999.99
    
    def place_items(self):
        return f"You placed items on a {self.style} table."
    
    def get_description(self):
        return f"{self.style} Table - Material: {self.material}, Price: ${self.price}"

#===================================================================================================================#
#Sofa Implementations
#===================================================================================================================#
class ModernSofa(ISofa):
    def __init__(self):
        self.style = "Modern"
        self.material = "Microfiber"
        self.price = 899.99
    
    def relax_on(self):
        return f"You are relaxing on a {self.style} sofa."
    
    def get_description(self):
        return f"{self.style} Sofa - Material: {self.material}, Price: ${self.price}"

class VictorianSofa(ISofa):
    def __init__(self):
        self.style = "Victorian"
        self.material = "Velvet"
        self.price = 1299.99
    
    def relax_on(self):
        return f"You are relaxing on a {self.style} sofa."
    
    def get_description(self):
        return f"{self.style} Sofa - Material: {self.material}, Price: ${self.price}"

class ArtDecoSofa(ISofa):
    def __init__(self):
        self.style = "Art Deco"
        self.material = "Silk"
        self.price = 1599.99
    
    def relax_on(self):
        return f"You are relaxing on a {self.style} sofa."
    
    def get_description(self):
        return f"{self.style} Sofa - Material: {self.material}, Price: ${self.price}"
