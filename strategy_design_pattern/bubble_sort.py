from sorting_strategy_interface import SortingStrategy
from typing import List

class BubbleSort(SortingStrategy): 
    
    def __init__(self): 
        self.__name = "Bubble_Sort"

    def sort(self, arr: List[int]):
        if len(arr) == 0: 
            return 
        for j in range(1, len(arr)):
            for i in range(len(arr)-j): 
                if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    
    @property
    def name(self) -> str: 
        return self.__name 
