class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, current_sum):
            if not node:
                return

            path.append(node.val)
            current_sum += node.val

            # Check if it's a valid root-to-leaf path
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path[:])  # add a copy of the current path

            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)

            path.pop()  # backtrack

        dfs(root, [], 0)
        return result

            
