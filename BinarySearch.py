from turtle import right
from typing import List

numsArray: List[int] = []

for i in range(500):
    numsArray.append(i)

def BinarySearch(num: int, arr: List[int], sorted: bool = True) -> int:
    if sorted is False:
        arr.sort()
        
    count: int = 0
    
    left, right = 0, len(arr) - 1
    
    if num > arr[right]:
        print("Error Number")
        return -1

    while left <= right:
        count += 1
        mid =  (int) ((left + right) / 2)
        midEle = arr[mid]
    
        if midEle == num:
            print("ITERATION: ", count)
            return mid

        elif midEle < num:
            left = mid + 1 

        elif midEle > num:
            right = mid - 1
    
    return -1

def BinarySearchRecursion(num: int, arr: List[int], sorted: bool = True) -> int:

    left = 0
    right = len(arr) - 1

    if sorted == False:
            arr.sort()
    
    def _BinarySearchRecursion(num: int, arr: List[int], l: int, r:int) -> int:
        mid = (int) ((l + r) / 2)
        
        if (arr[r] < num) or (r < l):
            print("NOT FOUND")
            return -1

        if arr[mid] == num:
            return mid
        
        if arr[mid] < num:
            return _BinarySearchRecursion(num, arr, mid + 1, r)
        
        if arr[mid] > num:
            return _BinarySearchRecursion(num, arr, l, mid - 1, )
        
        return -1
    
    return _BinarySearchRecursion(num, arr, left, right)

res = BinarySearchRecursion(50, numsArray)
print(res)