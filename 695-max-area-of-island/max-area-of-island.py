class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = 2
            size = 1
            while queue:
                dr,dc = queue.popleft()
                for ro,co in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = dr+ro, dc+co
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        size+=1
            return size
        
        maxSize = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxSize = max(maxSize,bfs(r,c))

        return maxSize
