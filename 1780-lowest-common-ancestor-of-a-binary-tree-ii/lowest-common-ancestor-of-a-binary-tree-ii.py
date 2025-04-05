# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found_p=False
        found_q=False
        def dfs(root):
            nonlocal found_p
            nonlocal found_q
            if not root:
                return None
            left = dfs(root.left)
            right = dfs(root.right)

            if root==p:
                found_p = True
                return root
            if root==q:
                found_q = True
                return root

            if left and right:
                return root
            return left if left else right

        ans = dfs(root) 
        return ans if found_p and found_q else None