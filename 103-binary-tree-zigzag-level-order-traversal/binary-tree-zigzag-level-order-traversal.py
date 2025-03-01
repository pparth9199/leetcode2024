# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        zig = 0
        while queue:
            curr_level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if zig % 2 != 0:
                curr_level[:] = curr_level[::-1]
            zig += 1
            levels.append(curr_level)
        return levels