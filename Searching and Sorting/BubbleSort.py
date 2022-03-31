from typing import List


def BubbleSort(arr: List[int]):
    length = len(arr)

    for i in range(length):
        breakOut = 0

        for j in range(length - i - 1):
            k = j + 1

            if k < length and arr[j] > arr[k]:
                temp = arr[j]
                arr[j] = arr[k]
                arr[k] = temp
                breakOut = 1
                
        if breakOut == 0:
            break

    return arr


# array = [8, 3, 6, 4, 5]
array = ['manu', 'prajwal', 'aradhya']

# for i in range(20):
#     array.append(random.randint(0, 100))

print("Original: ", array)

print("Sorted: ", BubbleSort( array ))