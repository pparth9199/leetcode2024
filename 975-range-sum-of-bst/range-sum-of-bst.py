# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            if root.val>=low and root.val<=high:
                res += root.val
                dfs(root.left)
                dfs(root.right)
            elif root.val < low:
                dfs(root.right) 
            else: 
                dfs(root.left) 
        dfs(root)
        return res
