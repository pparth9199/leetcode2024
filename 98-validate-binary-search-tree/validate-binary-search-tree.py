class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        previous = -inf
        def inorder(root):
            nonlocal previous
            if not root:
                return True
            left = inorder(root.left)
            if not left:
                return False
            if root.val <= previous:
                return False
            previous = root.val
            right = inorder(root.right)
            return right
        return inorder(root)