from abc import ABC, abstractmethod
from typing import List

class SortingStrategy: 
    
    @abstractmethod
    def sort(self, nums: List[int]): 
        pass
    
    @property
    @abstractmethod
    def name(): 
        pass