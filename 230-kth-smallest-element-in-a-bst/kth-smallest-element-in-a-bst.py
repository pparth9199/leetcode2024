# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current_node = 0
        res=None
        def dfs(root):
            nonlocal current_node,res
            if not root:
                return
            dfs(root.left)
            current_node+=1
            if k==current_node:
                res=root.val
            dfs(root.right)
        dfs(root)
        return res