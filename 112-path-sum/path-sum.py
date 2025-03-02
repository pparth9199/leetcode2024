# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, path, target):
            if not root:
                return False
            path = path + root.val
            if not root.left and not root.right:
                if path == target:
                    return True
            left = dfs(root.left, path, target)
            right = dfs(root.right, path, target)
            return left or right
        return dfs(root, 0, targetSum)