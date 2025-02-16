# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def treeHeight(node):
            if node == None:
                return 0
            l = treeHeight(node.left)
            r = treeHeight(node.right)
            if l == -1 or r == -1:
                return -1
            if abs(l-r) > 1:
                return -1
            return max(l,r) + 1
        return treeHeight(root) != -1
            

        