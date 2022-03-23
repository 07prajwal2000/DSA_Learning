from typing import List

def RemoveDuplicates(nums: List[int]) -> int:
    left = 1
    for right in range(1, len(nums)):
        if nums[right - 1] != nums[right]:
            nums[left] = nums[right]
            left += 1

    return left

print(RemoveDuplicates([0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 5]))
print(RemoveDuplicates([1,2,2]))