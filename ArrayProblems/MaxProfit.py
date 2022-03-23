from typing import List

array: List[int] = [7, 3, 5, 3, 6, 8]

def CalculateProfit(prices: List[int]):
    left, right = 0, 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1
    
    return max_profit


print(CalculateProfit(array))