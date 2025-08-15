from bubble_sort import BubbleSort
from quick_sort import QuickSort
from context_sorter import Sorter

def main(): 
    sorter = Sorter()
    
    # sorting with bubble strategy 
    bubble_sort = BubbleSort()
    arr = [1,2,3,6,7,5]
    sorter.set_strategy(bubble_sort)
    sorter.sort(arr)

    # sorting with the quick sort strategy
    quick_sort = QuickSort()
    arr = [1,2,3,6,7,5]
    sorter.set_strategy(quick_sort)
    sorter.sort(arr)

if __name__ == "__main__": 
    main()



