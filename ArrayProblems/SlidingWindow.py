from typing import List

class AvgSumSubArray:

    def Brute_Force(self, arr: List[int], k): # Returns Sub array of Avg wrt k
        avgs = []
        length = len(arr) - k + 1

        for i in range(length):
            sum = 0

            for j in range(k):
                sum += arr[i + j]
            avgs.append(sum / k)
        
        return avgs #Brute-Force Method

    def Optimized(self, arr, k):
        avgs = []
        prevIndex = 0
        sum = 0

        for i in range(len(arr)):
            sum += arr[i]
            
            if i >= k - 1:
                avgs.append(sum / k)
                sum -= arr[prevIndex]
                prevIndex += 1

        return avgs




# TESTS #
def TestAvgSumSubArray():
    array = [1, 2, 3, 4, 5]

    # for i in range(6, 1000000): # 1 Million Iter's
    #     array.append(i)
    # print("Filling List < COMPLETEED >")
    
    avgSum = AvgSumSubArray()
    res = avgSum.Optimized(array, 3)
    print(res)

TestAvgSumSubArray()