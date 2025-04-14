class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(node, depth):
            if not node:
                return
            # First time reaching this depth
            if depth == len(result):
                result.append(node.val)
            # Visit right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result