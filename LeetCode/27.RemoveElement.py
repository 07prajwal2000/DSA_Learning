from typing import List


def RemoveElement(nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if val != nums[i]:
            nums[count] = nums[i]
            count += 1
    return count, nums

print(RemoveElement([3,2,2,3], 2))