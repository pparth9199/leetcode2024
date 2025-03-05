# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minimum= inf
        def dfs(root):
            nonlocal minimum
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if not root.left or not root.right:
                return max(left, right) + 1  
            return min(left,right)+1
        return dfs(root)
            