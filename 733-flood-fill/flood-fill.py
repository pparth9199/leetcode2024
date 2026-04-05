class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        before = image[sr][sc]

        def bfs(r,c):
            queue = deque([(r,c)])
            image[r][c]=color

            while queue:
                dr,dc = queue.popleft()
                for row,col in ([(-1,0),(0,1),(1,0),(0,-1)]):
                    nr,nc = dr+row,dc+col
                    if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==before and image[nr][nc]!=color:
                        image[nr][nc]=color
                        queue.append([nr,nc])
                
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=before or image[r][c]==color:
                return
            image[r][c] = color

            for rw,clm in ([(-1,0),(1,0),(0,-1),(0,1)]):
                dfs(r+rw,c+clm)

        bfs(sr,sc)
        return image