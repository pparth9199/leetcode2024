# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def parse(root):
            if not root:
                return 0
            left=0
            right=0
            left = max(left, parse(root.left))
            right = max(right,parse(root.right))
            
            self.maxSum = max(self.maxSum,left+right+root.val)
            return root.val + max(left,right)
        self.maxSum = float('-inf')
        parse(root)
        return self.maxSum