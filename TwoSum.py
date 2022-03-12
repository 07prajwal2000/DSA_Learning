from typing import List

def TwoSum(targetSum: int, array: List[int]):
    foundElements = {}
    for i, num in enumerate(array):
        diff = targetSum - num
        if diff in foundElements:
            return [foundElements[targetSum - num], i]
        
        foundElements[num] = i

    return

arr = [2,7,11,15]

for i in range(1000000):
    arr.append(i)

print(TwoSum(665878, arr))