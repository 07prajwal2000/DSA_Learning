from operator import le
from typing import List

def SetZeroMatrix(matrix: List[List[int]]):
    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                idx = 0
                while idx < row:
                    if matrix[idx][j] != 0:
                        matrix[idx][j] = -1
                    idx += 1

                idx = 0
                while idx < column:
                    if matrix[i][idx] != 0:
                        matrix[i][idx] = -1
                    idx += 1
    for i in range(row):
        for j in range(column):
            if matrix[i][j] < 0:
                matrix[i][j] = 0

def V2(matrix: List[List[int]]):
    row = len(matrix)
    column = len(matrix[0])
    rowArr = [1] * (row)
    columnArr = [1] * (column)

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                rowArr[i] = 0
                columnArr[j] = 0
    for i in range(row):
        for j in range(column):
            if rowArr[i] == 0 or columnArr[j] == 0:
                matrix[i][j] = 0



matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
for i in matrix:
    print(i)
print('\n')
print('\n')
V2(matrix)
for i in matrix:
    print(i)