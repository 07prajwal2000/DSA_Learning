from typing import List


def MoveZeros(nums: List[int]):
    i = 0
    a = 0
    while i < len(nums):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[a]
            nums[a] = temp
            a += 1
        i += 1
    return nums

print(MoveZeros([0,1,0,3,12]))