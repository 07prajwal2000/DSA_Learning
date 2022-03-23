from typing import List

def FindDuplicate(arr: List[int]):
    duplicate = {}
    for x in enumerate(arr):
        if duplicate[x] is not None:
            return x
        duplicate[x] = True
    return

array = [1, 2, 4, 8, 3, 5, 8, 6]
print(FindDuplicate(array))