from typing import List


def RotateArray(nums: List[int], k: int):
    temp = [0] * len(nums)
    for i in range(len(nums)):
        idx = (i + k) % len(nums)
        temp[idx] = nums[i]
    nums.clear()
    nums.extend(temp)

arr = [1,2,3,4,5,6,7]
RotateArray(arr, 3)
print(arr)

arr = [-1, -100, 3, 99]
RotateArray(arr, 2)
print(arr)
