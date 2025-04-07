class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(queue):
            minutes = 0
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
                if queue:
                    minutes += 1
            return minutes

        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        res = bfs(queue)

        # Check for any remaining fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return res