from furniture_abstract_factory import FurnitureFactory
from modern_chair import ModernChair
from modern_table import ModernTable

class ModernFurnitureFactory(FurnitureFactory): 
    def create_table(self)-> ModernTable:
        print("Creating the Modern Table....")
        return ModernTable()

    def create_chair(self) -> ModernChair:         
        print("Creating the Modern Chair....")
        return ModernChair()
    