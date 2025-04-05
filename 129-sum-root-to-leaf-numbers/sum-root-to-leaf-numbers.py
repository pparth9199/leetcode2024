# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        res = []
        summ =0

        def dfs(root):
            nonlocal stack 
            nonlocal summ
            nonlocal res

            if not root:
                return None
            stack.append(str(root.val))
            if not root.left and not root.right:
                summ+=int("".join(stack))
            else:
                dfs(root.left)
                dfs(root.right)
            stack.pop()

        dfs(root)

        return summ
            
