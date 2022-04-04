from typing import List


def ReverseArray(arr: List[int]):
    l, r = 0, len(arr) - 1
    while l <= r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l += 1
        r -= 1
    return arr

array = [1, 2, 3, 4, 5]
print(ReverseArray(array))