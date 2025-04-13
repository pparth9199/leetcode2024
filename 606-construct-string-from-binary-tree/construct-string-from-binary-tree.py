# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        def dfs(root):
            nonlocal res
            if not root:
                return
            
            res+=str(root.val)
            if not root.left and root.right:
                res+="()"
            if root.left:
                res+="("
                dfs(root.left)
                res+=")"
            if root.right:
                res+="("
                dfs(root.right)
                res+=")"
            

        dfs(root)
        return res