class Solution:
    def minPathSum(self, grid):
        colLen = len(grid)
        column = [-1] * colLen
        column[0] = grid[0][0]
        for index in range(1, colLen):
            column[index] = grid[index][0] + column[index-1]
        for colIndex in range(1, len(grid[0])):
            column[0] += grid[0][colIndex]
            for rowIndex in range(1, colLen):
                column[rowIndex] = min(column[rowIndex], column[rowIndex-1])+ grid[rowIndex][colIndex]
        return column[-1]