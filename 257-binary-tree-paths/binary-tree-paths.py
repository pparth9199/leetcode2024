# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            nonlocal paths
            if not node:
                return None
            path = path + str(node.val)
            if not node.left and not node.right:
                paths.append(path)
                path = ""
            else:
                path = path + "->"
                dfs(node.left, path)
                dfs(node.right, path)
        paths = []
        dfs(root, "")
        return paths