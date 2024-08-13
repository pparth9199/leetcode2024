# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def parse(root):
            if not root:
                return 1
            if root.right!=None and root.left==None:
                return 0
            left = parse(root.left)
            right = parse(root.right)
            
            return left+right
        
        return parse(root)-1
            