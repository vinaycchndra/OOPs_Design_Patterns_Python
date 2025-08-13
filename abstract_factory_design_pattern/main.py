from modern_furniture_factory import ModernFurnitureFactory
from victorian_furniture_factory import VictorianFurnitureFactory

def main(): 
    modern_factory = ModernFurnitureFactory()
    modern_factory.create_chair()
    modern_factory.create_table()

    victorian_factory = VictorianFurnitureFactory()
    victorian_factory.create_chair()
    victorian_factory.create_table()


if __name__ == "__main__": 
    main()


