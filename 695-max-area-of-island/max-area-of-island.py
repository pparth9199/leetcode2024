class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        a = 0
        ans = 0

        def dfs(r,c):
            nonlocal a
            grid[r][c] = 2
            if r > 0:
                if grid[r-1][c] == 1:
                    a = a + 1
                    dfs(r-1,c)
            if r < R - 1:
                if grid[r+1][c] == 1:
                    a = a + 1
                    dfs(r+1,c)
            if c > 0:
                if grid[r][c-1] == 1:
                    a = a + 1
                    dfs(r,c-1)
            if c < C - 1:
                if grid[r][c+1] == 1:
                    a = a + 1
                    dfs(r,c+1)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    a = 1
                    dfs(i,j)
                    ans = max(ans, a)
        return ans