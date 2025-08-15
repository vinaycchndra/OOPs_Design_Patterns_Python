from sorting_strategy_interface import SortingStrategy
from typing import List

class BubbleSort(SortingStrategy): 
    
    def __init__(self): 
        self.__name = "Bubble_Sort"

    def sort(self, nums: List[int]):
        pass
    
    @property
    def name(self) -> str: 
        return self.__name 
