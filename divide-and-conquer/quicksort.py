from typing import List

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def parition(arr: List[int], left: int, right: int):
    
    pivot = (left + right) // 2
    arr = swap(arr, pivot, len(arr) - 1)
    pivot = right
    i = left
    j = pivot - 1

    while i < j:
        if arr[i] < pivot:
            i += 1
        if j > pivot:
            j += 1
        
        swap(i, right)

        


def quicksort(arr: List[int]) -> List[int]:
    parition(arr, 0, len(arr) - 1)    

quicksort([7, 3, 1, 4, 2, 6, 5])