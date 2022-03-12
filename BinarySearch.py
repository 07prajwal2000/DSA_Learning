from typing import List

numsArray: List[int]

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


res = BinarySearch(50, numsArray, True)
print(res)