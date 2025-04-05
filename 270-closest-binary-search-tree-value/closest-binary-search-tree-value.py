# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_val = root.val
        def dfs(root):
            nonlocal min_val
            if not root:
                return

            if (abs(root.val - target) < abs(min_val - target) or (abs(root.val - target) == abs(min_val - target) and root.val < min_val)):
                min_val = root.val
            
            if target < root.val:
                dfs(root.left)
            else:
                dfs(root.right)

        dfs(root)
        return min_val
