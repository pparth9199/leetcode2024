# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, low=-inf, high=inf):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            left = valid(root.left, low, root.val)
            right = valid(root.right, root.val, high)
            return left and right
        return valid(root)