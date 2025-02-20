class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return None
        
        time = 0
        fresh = 0
        R = len(grid)
        C = len(grid[0])
        queue = deque()
        directions = [[0,-1], [-1,0], [0,1], [1,0]]
                
        for m in range(R):
            for n in range(C):
                if grid[m][n] == 2:
                    queue.append((m,n))
                elif grid[m][n] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            lenq = len(queue)
            isRot = 0
            for _ in range(lenq):
                i,j = queue.popleft()

                for dr, dc in directions:
                    row, col = i + dr, j + dc
                    if row < 0 or row > R-1 or col < 0 or col > C-1:
                        continue
                    if grid[row][col] == 1:
                        isRot = 1
                        fresh -= 1
                        grid[row][col] = 2
                        queue.append((row,col))
            if isRot == 1:
                time = time + 1

        if fresh:
            return -1
        return time
        



