class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            queue = deque([(r, c)])
            grid[r][c] = "2"
            size =1 
            while queue:
                dr,dc = queue.popleft()
                for rw,cm in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr,nc = dr+rw,dc+cm
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1":
                        grid[nr][nc]="2"
                        size+=1
                        queue.append([nr,nc])
            return size

        def dfs(r,c):
            if c<0 or r<0 or c>=cols or r>=rows or grid[r][c]!="1":
                return 0
            grid[r][c]="2"
            size = 1 
            for row,col in [(-1,0),(0,-1),(1,0),(0,1)]:
                size+= dfs(r+row,c+col)
            return size
            
        count = 0
        sizes = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    #sizes.append(bfs(r, c))
                    sizes.append(dfs(r,c))
        return count
