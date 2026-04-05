"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

"""
- Grid is nxn
- We take top left as 0,0
- we take top right as n/2,0
- we take bottom left as 0,n/2
- we take bottom right as n/2,n/2
- we need to check if all the values are same it is redundant to recurse over it
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid)
        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                prefix[i+1][j+1] = grid[i][j]+prefix[i][j+1]+prefix[i+1][j]-prefix[i][j]
        
        def getSum(r,c,n):
            return prefix[r+n][c+n]-prefix[r][c+n]-prefix[r+n][c]+prefix[r][c] 

        def dfs(n,r,c):
            total = getSum(r,c,n)
            if total==0:
                return Node(0,True)
            if total==n*n:
                return Node(1,True)

            n=n//2
            tl = dfs(n,r,c)
            tr = dfs(n,r,c+n)
            bl = dfs(n,r+n,c)
            br = dfs(n,r+n,c+n)

            return Node(0,False,tl,tr,bl,br)

        return dfs(len(grid),0,0)