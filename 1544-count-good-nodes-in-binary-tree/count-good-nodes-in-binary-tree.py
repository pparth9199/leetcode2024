# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(root,maxx):
            nonlocal good
            if not root:
                return

            if root.val>=maxx:
                good+=1
                maxx=root.val

            dfs(root.left,maxx)
            dfs(root.right,maxx)

        dfs(root,root.val)
        return good