# Starter Code - Furniture Shop (Python)
# This code demonstrates a tightly coupled design that needs refactoring
# using the Abstract Factory pattern

from typing import List

class Chair:
    """Basic chair class - current implementation"""
    
    def __init__(self, style: str, material: str, price: float):
        self.style = style
        self.material = material
        self.price = price
    
    def sit_on(self):
        print(f"Sitting on a {self.style} chair made of {self.material}")
    
    def get_description(self) -> str:
        return f"{self.style} chair made of {self.material} - ${self.price}"


class Table:
    """Basic table class - current implementation"""
    
    def __init__(self, style: str, material: str, price: float):
        self.style = style
        self.material = material
        self.price = price
    
    def place_items(self):
        print(f"Placing items on a {self.style} table made of {self.material}")
    
    def get_description(self) -> str:
        return f"{self.style} table made of {self.material} - ${self.price}"


class Sofa:
    """Basic sofa class - current implementation"""
    
    def __init__(self, style: str, material: str, price: float):
        self.style = style
        self.material = material
        self.price = price
    
    def relax_on(self):
        print(f"Relaxing on a {self.style} sofa made of {self.material}")
    
    def get_description(self) -> str:
        return f"{self.style} sofa made of {self.material} - ${self.price}"


class FurnitureShop:
    """The problematic FurnitureShop class - tightly coupled!"""
    
    def __init__(self):
        self.chairs: List[Chair] = []
        self.tables: List[Table] = []
        self.sofas: List[Sofa] = []
    
    def create_furniture_set(self, style: str):
        """This method violates the Open/Closed Principle
        Adding new styles requires modifying this code"""
        
        style = style.lower()
        
        if style == "modern":
            self.chairs.append(Chair("Modern", "Steel and Leather", 299.99))
            self.tables.append(Table("Modern", "Glass and Chrome", 599.99))
            self.sofas.append(Sofa("Modern", "Microfiber", 899.99))
        elif style == "victorian":
            self.chairs.append(Chair("Victorian", "Mahogany", 499.99))
            self.tables.append(Table("Victorian", "Oak", 799.99))
            self.sofas.append(Sofa("Victorian", "Velvet", 1299.99))
        elif style == "artdeco":
            self.chairs.append(Chair("Art Deco", "Walnut", 399.99))
            self.tables.append(Table("Art Deco", "Marble and Brass", 999.99))
            self.sofas.append(Sofa("Art Deco", "Silk", 1599.99))
        else:
            print(f"Unknown furniture style: {style}")
    
    def display_inventory(self):
        """Display all furniture in the shop"""
        print("=== FURNITURE SHOP INVENTORY ===")
        print("Chairs:")
        for chair in self.chairs:
            print(f"  {chair.get_description()}")
        print("Tables:")
        for table in self.tables:
            print(f"  {table.get_description()}")
        print("Sofas:")
        for sofa in self.sofas:
            print(f"  {sofa.get_description()}")
    
    def demonstrate_furniture(self):
        """Demonstrate the furniture functionality"""
        print("=== FURNITURE DEMONSTRATION ===")
        if self.chairs:
            self.chairs[0].sit_on()
        if self.tables:
            self.tables[0].place_items()
        if self.sofas:
            self.sofas[0].relax_on()


def main():
    """Client code that uses the furniture shop"""
    shop = FurnitureShop()
    
    # Create different furniture sets
    shop.create_furniture_set("modern")
    shop.create_furniture_set("victorian")
    shop.create_furniture_set("artdeco")
    
    # Display the inventory
    shop.display_inventory()
    
    # Demonstrate the furniture
    shop.demonstrate_furniture()


if __name__ == "__main__":
    main()

"""
PROBLEMS WITH THIS CODE:
1. Tight Coupling: The FurnitureShop class is tightly coupled to concrete furniture classes
2. Violation of Open/Closed Principle: Adding new styles requires modifying existing code
3. Code Duplication: Similar creation logic is repeated for each style
4. Hard to Maintain: Changes to one style might affect others
5. No Abstraction: No common interface for furniture types

YOUR TASK:
Refactor this code using the Abstract Factory pattern to:
- Create abstract base classes/interfaces for each furniture type
- Implement concrete classes for each style
- Create an abstract factory interface
- Implement concrete factories for each style
- Modify the client to use the factory pattern
"""

