# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nextLevel = deque([root])
        res = []
        flip = True  # True = left to right, False = right to left

        while nextLevel:
            current = nextLevel
            nextLevel = deque()
            current_level = []

            while current:
                node = current.popleft()
                current_level.append(node.val)

                # Always add children in normal order (left first)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            # Reverse the current level if flip is False
            if not flip:
                current_level.reverse()

            res.append(current_level)
            flip = not flip 
        return res
                    