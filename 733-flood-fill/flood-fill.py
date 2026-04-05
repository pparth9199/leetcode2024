class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        before = image[sr][sc]
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=before or image[r][c]==color:
                return
            image[r][c] = color

            for rw,clm in ([(-1,0),(1,0),(0,-1),(0,1)]):
                dfs(r+rw,c+clm)

        dfs(sr,sc)
        return image