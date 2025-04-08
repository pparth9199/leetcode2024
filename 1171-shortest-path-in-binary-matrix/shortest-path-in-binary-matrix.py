class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])

        
        if grid[0][0] !=0 or grid[-1][-1]!=0:
            return -1


        def bfs(r,c):
            queue = deque([(0,0,1)])
            grid[r][c] = 1

            directions = [(0,-1),(0,1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

            while queue:
                dr,dc,dist = queue.popleft()

                if dr==rows-1 and dc == cols-1:
                    return dist

                for r,c in directions:
                    nr,nc = dr+r,dc+c

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr,nc,dist+1))

            return -1
        return bfs(0,0)
        
        