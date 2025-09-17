# Starter Code - Furniture Shop (Python)
# This code demonstrates a tightly coupled design that needs refactoring
# using the Abstract Factory pattern

from typing import List
from concreteFurniture import *
from concreteFactory import *

class FurnitureShop:
    """The problematic FurnitureShop class - tightly coupled!"""
    
    def __init__(self):
        self.chairs: List = []
        self.tables: List = []
        self.sofas: List = []
    
    def create_furniture_set(self, style: str):
        """This method violates the Open/Closed Principle
        Adding new styles requires modifying this code"""
        
        style = style.lower()
        
        #new styles can be added more easily using the Abstract Factory pattern
        if style == "modern":
            factory = ModernFurnitureFactory()
            self.chairs.append(factory.createChair())
            self.tables.append(factory.createTable())
            self.sofas.append(factory.createSofa())
        elif style == "victorian":
            factory = VictorianFurnitureFactory()
            self.chairs.append(factory.createChair())
            self.tables.append(factory.createTable())
            self.sofas.append(factory.createSofa())
        elif style == "artdeco":
            factory = ArtDecoFurnitureFactory()
            self.chairs.append(factory.createChair())
            self.tables.append(factory.createTable())
            self.sofas.append(factory.createSofa())
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

