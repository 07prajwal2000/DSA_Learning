from typing import List


def MergeTwoSortedArrays(nums1: List[int], nums2: List[int], m, n):
    a, b = 0, 0
    result = []
    while a < m and b < n:
        if nums1[a] > nums2[b]:
            result.append(nums2[b])
            b += 1
        else:
            result.append(nums1[a])
            a += 1
    
    while a < m:
        result.append(nums1[a])
        a += 1

    while b < n:
        result.append(nums2[b])
        b += 1
    return result

def AcceptedAnswer(nums1: List[int], m: int, nums2: List[int], n: int):
    temp1 = nums1[:m]
    nums1.clear()
    temp2 = nums2[:n]
    temp1.extend(temp2)
    temp1.sort()
    nums1.extend(temp1)

print(MergeTwoSortedArrays( [0], [1], 0, 1 ) )