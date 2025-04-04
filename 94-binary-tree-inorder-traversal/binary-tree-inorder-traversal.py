# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root,ans):
            if not root:
                return []
            left = dfs(root.left,ans)
            ans.append(root.val)
            right = dfs(root.right,ans)

            return ans
        return dfs(root,[])