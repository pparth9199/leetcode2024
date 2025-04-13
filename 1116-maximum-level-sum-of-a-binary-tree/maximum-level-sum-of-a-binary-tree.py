# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        current_level = 0
        max_sum = root.val
        max_level = 1

        while queue:
            curr = queue
            queue = deque()
            sum_level = 0
            current_level+=1
            while curr:
                node = curr.popleft()
                sum_level+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum_level>max_sum:
                max_sum = sum_level
                max_level = current_level
        return max_level


