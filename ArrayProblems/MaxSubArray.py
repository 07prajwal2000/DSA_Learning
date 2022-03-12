from sys import maxsize
from typing import List


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def MaxSubArray(arr: List[int]):
    maxSub = arr[0]
    curSum = 0
    for n in arr:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(curSum, maxSub)
    return maxSub

print(MaxSubArray(array))