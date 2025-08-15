from sorting_strategy_interface import SortingStrategy
from typing import List

class QuickSort(SortingStrategy): 

    def __init__(self): 
        self.__name = "Quick_Sort"

    def sort(self, nums: List[int]):
        self.__sort_arr(nums, 0, len(nums)-1)
       
    def __partition(self, i: int, j: int, arr: List[int]) -> int: 
        index = i-1
        for k in range(i, j): 
            if arr[k] <= arr[j]: 
                index += 1
                arr[k], arr[index] = arr[index], arr[k]
        index += 1 
        arr[index], arr[j] = arr[j], arr[index]
        return index

    def __sort_arr(self, arr: List[int], i : int, j: int): 
        if i >= j: 
            return 
        index = self.__partition(i, j, arr)
        
        self.__sort_arr(arr, i, index-1)
        self.__sort_arr(arr, index+1, j)

    @property
    def name(self) -> str: 
        return self.__name 