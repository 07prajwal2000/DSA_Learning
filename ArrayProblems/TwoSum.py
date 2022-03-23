from typing import List

def TwoSum(target: int, nums: List[int]):
    foundElements = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in foundElements:
            return [foundElements[target - num], i]
        
        foundElements[num] = i

    return

array = [2, 3, 5, 6, 7, 11, 15, 16, 12]

# for i in range(1000000):
#     arr.append(i)


def Test(target, nums: List[int]):
    hashMap = {}
    i = 0
    for num in nums:
        difference = target - num
        if difference in hashMap:
            return [i, hashMap[difference]]
        hashMap[num] = i
        i += 1
    return

print(Test(6, [3, 2, 4]))