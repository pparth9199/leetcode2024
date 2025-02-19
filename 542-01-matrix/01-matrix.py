class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        
        R = len(mat)
        C = len(mat[0])

        res = [[float('inf')] * C for i in range(R)]
        queue = deque()

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i,j))
        
        directions = [[-1,0], [0, -1], [1,0], [0,1]]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < R and 0 <= col < C and res[row][col] > res[r][c] + 1:
                    res[row][col] = res[r][c] + 1
                    queue.append((row, col))
        return res
        