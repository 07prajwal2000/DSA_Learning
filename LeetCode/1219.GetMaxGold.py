from typing import List
from xmlrpc.client import boolean


def GetMaximumGold(grid: List[List[int]]) -> int:
    if grid is None or len(grid) is 0:
        return 0
    
    maxGold, x, y = 0, len(grid), len(grid[0])
    for i in range(x):
        for j in range(y):
            if grid[x][y] > 0:
                gold: int = FindMaxGold(grid, i, j, x, y, [[]])
                maxGold = max(maxGold, gold)
    
    return maxGold

# def FindMaxGold(grid: List[List[int]], i, j, x, y, boolGrid: List[List[boolean]]) -> int:
    

# print(GetMaximumGold([[0,6,0], [5,8,7], [0,9,0]]) )