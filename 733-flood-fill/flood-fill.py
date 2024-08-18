class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        def dfs(r,c,grid,currentColor):
            if r<0 or c<0 or r>len(grid)-1 or c>len(grid[0])-1:
                return 

            if grid[r][c]!=currentColor:
                return
            grid[r][c] = color

            dfs(r-1,c,grid,currentColor)
            dfs(r+1,c,grid,currentColor)
            dfs(r,c-1,grid,currentColor)
            dfs(r,c+1,grid,currentColor)
            return grid
        return dfs(sr,sc,image,image[sr][sc])