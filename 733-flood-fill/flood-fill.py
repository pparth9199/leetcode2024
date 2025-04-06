class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        if old_color == color:
            return image
        
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=old_color:
                return

            image[r][c] = color

            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(r+dr,c+dc)

        
        dfs(sr, sc)
        return image
