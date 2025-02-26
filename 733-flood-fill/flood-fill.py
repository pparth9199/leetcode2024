class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)  - 1
        n = len(image[0]) - 1
        initial = image[sr][sc]
        if initial == color:
            return image
        def dfs(r,c):
            image[r][c] = color
            if r > 0:
                if image[r-1][c] == initial:
                    dfs(r-1, c)
            if r < m:
                if image[r+1][c] == initial:
                    dfs(r+1, c)
            if c > 0:
                if image[r][c-1] == initial:
                    dfs(r, c-1)
            if c < n:
                if image[r][c+1] == initial:
                    dfs(r, c+1)
        dfs(sr,sc)
        return image