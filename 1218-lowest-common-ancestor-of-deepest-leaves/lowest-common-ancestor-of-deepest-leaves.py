# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dist = 0
        max_dist = -1
        res=None
        def dfs(root,dist):
            nonlocal max_dist,res
            if not root:
                max_dist = max(max_dist,dist)
                return dist
            left = dfs(root.left,dist+1)
            right = dfs(root.right,dist+1)
            if left==right and left == max_dist:
                res = root
            return max(left,right) 

        dfs(root,0)
        return res