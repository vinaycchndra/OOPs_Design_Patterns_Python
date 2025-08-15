from sorting_strategy_interface import SortingStrategy

# This is the context class which actually executes the sorting logic... 
class Sorter: 
    def __init__(self): 
        self.__sorter = None

    def sort(self, nums): 
        if self.__sorter is None: 
            raise Exception("Sorting strategy not set")
        self.__sorter.sort(nums)
        print(f"Successfully sorted the nums... with {self.__sorter.name}")

    def set_strategy(self, strategy: SortingStrategy): 
        self.__sorter = strategy


