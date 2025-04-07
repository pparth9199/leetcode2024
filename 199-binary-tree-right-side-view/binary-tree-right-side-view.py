class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        nex_level = deque([root])
        right = []
        while nex_level:
            current = nex_level
            nex_level = deque()

            while current:
                node = current.popleft()
                if node.left:
                    nex_level.append(node.left)
                if node.right:
                    nex_level.append(node.right)

            right.append(node.val)
        return right