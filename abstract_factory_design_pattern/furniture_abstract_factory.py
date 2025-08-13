from abc import ABC, abstractmethod


class FurnitureFactory(ABC): 
    
    @abstractmethod
    def create_table(): 
        pass

    @abstractmethod
    def create_chair(): 
        pass
