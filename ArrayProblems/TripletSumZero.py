from typing import List


def TripletSumZero(arr: List[int], targetSum: int = 0):
    arr.sort();
    result = []
    for i in range(len(arr)):
        left, right = i + 1, len(arr) - 1

        # Checking for Duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        while left < right:
            leftEle, rightEle = arr[left], arr[right]
            sum = arr[i] + leftEle + rightEle

            if sum == targetSum:
                result.append([ arr[i], leftEle, rightEle ])
                left += 1
                right -= 1
                
                # Avoiding Duplication
                while left < right and leftEle == arr[left + 1]:
                    left += 1
                
                while left < right and rightEle == arr[right - 1]:
                    right -= 1
                
            elif sum > targetSum:
                right -= 1
            
            else:
                left += 1

    return result

print(TripletSumZero([-3, 0, 1, 2, -1, 1, -2], 0))
print(TripletSumZero([-5, 2, -1, -2, 3], 0))