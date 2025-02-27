# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            # Calculate the number of good pairs with nodes from left and right subtrees
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        nonlocal count
                        count += 1

            # Return distances to the current node's parent
            result = []
            for d in left_distances + right_distances:
                if d < distance:
                    result.append(d + 1)
            return result

        count = 0
        dfs(root)
        return count