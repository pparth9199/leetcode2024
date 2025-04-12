class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        previous = -inf
        def dfs(root):
            nonlocal previous
            if not root:
                return True
            left = dfs(root.left)
            if not left:
                return False

            if root.val<=previous:
                return False
            
            previous = root.val

            right  = dfs(root.right)
            return right

        return dfs(root)