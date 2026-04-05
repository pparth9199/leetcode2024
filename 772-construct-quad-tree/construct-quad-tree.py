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
        def dfs(n,r,c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[r][c],True)

            n=n//2
            tl = dfs(n,r,c)
            tr = dfs(n,r,c+n)
            bl = dfs(n,r+n,c)
            br = dfs(n,r+n,c+n)

            return Node(0,False,tl,tr,bl,br)

        return dfs(len(grid),0,0)