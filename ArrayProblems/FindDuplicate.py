from typing import List

def FindDuplicate(arr: List[int]):
    duplicate = {}
    for x in range(len(arr)):
        if duplicate.get(arr[x]) is not None:
            duplicate[arr[x]] += 1
        else:
            duplicate[arr[x]] = 1
    return duplicate.values()

array = [1, 2, 4, 8, 3, 5, 8, 6]
print(FindDuplicate(array))