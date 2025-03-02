# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, path, pathSum):
            nonlocal ans
            if not node:
                return
            pathSum = pathSum + node.val
            path.append(node.val)
            if not node.left and not node.right:
                if pathSum == targetSum:
                    ans.append(path.copy())
            dfs(node.left, path, pathSum)
            dfs(node.right, path, pathSum)
            path.pop()
        dfs(root, [], 0)
        return ans