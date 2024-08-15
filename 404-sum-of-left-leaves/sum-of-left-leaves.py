# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sumLeft=0
        def parse(root):
            nonlocal sumLeft
            if not root:
                return 0
            if not root.right and not root.left:
                return root.val
            left = parse(root.left)
            sumLeft+=left if left else 0
            right = parse(root.right)
            
        parse(root)
        return sumLeft