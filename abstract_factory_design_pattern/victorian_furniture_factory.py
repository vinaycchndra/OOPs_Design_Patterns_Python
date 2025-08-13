from furniture_abstract_factory import FurnitureFactory
from victorian_chair import VictorianChair
from victorian_table import VictorianTable

class VictorianFurnitureFactory(FurnitureFactory): 

    def create_table(self) -> VictorianTable:
        print("Created the Victorian Table....")
        return VictorianTable()

    def create_chair(self) -> VictorianChair:         
        print("Created the Victorian Chair....")
        return VictorianChair()