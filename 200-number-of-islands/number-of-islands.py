class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return count
        
        m = len(grid)
        n = len(grid[0])

        def dfs(r,c):
            grid[r][c] = "2"
            if r > 0:
                if grid[r-1][c] == "1":
                    dfs(r-1,c)
            if r < m-1:
                if grid[r+1][c] == "1":
                    dfs(r+1,c)
            if c > 0:
                if grid[r][c-1] == "1":
                    dfs(r,c-1)
            if c < n-1:
                if grid[r][c+1] == "1":
                    dfs(r, c+1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count = count + 1
                    dfs(i,j)
        return count