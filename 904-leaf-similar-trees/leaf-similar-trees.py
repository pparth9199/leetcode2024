# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        def dfs(root1):
            nonlocal res1,res2
            if not root1:
                return 
            if not root1.right and not root1.left:
                res1.append(root1.val)

            dfs(root1.left)
            dfs(root1.right)
        
        dfs(root1)
        res2=res1[:]
        res1=[]
        dfs(root2)
        return res1==res2
            