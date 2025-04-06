class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        def bfs(r,c):
            queue = deque([(r, c)])
            grid[r][c] = "2"
            size = 1

            while queue:
                dr,dc = queue.popleft()
                
                for row,col in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr,nc = dr+row,dc+col
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1":
                        grid[nr][nc]="2"
                        queue.append([nr,nc])
                        size+=1
            return size 

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!="1":
                return 0
            
            grid[r][c] = "2"
            size = 1

            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                size+=dfs(r+dr,c+dc)
            return size

        count = 0
        sizes = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    count+=1
                    sizes.append(bfs(r,c))
                    # sizes.append(dfs(r,c))
        return count
