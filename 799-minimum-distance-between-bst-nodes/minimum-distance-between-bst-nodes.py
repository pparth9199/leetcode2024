# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        cachedRoot = None
        ans = float('inf')
        def dfs(root):
            nonlocal cachedRoot
            nonlocal ans
            if not root:
                return 
            
            dfs(root.left)
            if cachedRoot:
                ans = min(ans, root.val - cachedRoot.val)
            cachedRoot = root
            dfs(root.right)
            return
        dfs(root)
        return ans


