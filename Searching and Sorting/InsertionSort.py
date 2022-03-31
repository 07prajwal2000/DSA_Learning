from typing import List


def InsertionSort(arr: List[int]):
    lenght = len(arr)

    for i in range(1, lenght):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]

            if arr[j] < temp:
                break
            j -= 1
            
        arr[j + 1] = temp
            
    return arr

print(InsertionSort([8, 3, 6, 4, 5]))