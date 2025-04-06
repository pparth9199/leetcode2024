# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        switch = False
        while queue:
            nex = queue
            queue = deque()
            current_level = []
            while nex:
                node = nex.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if switch and node.val%2!=0:
                    return False
                if not switch and node.val%2==0:
                    return False
                if switch and current_level and current_level[-1] <= node.val:
                    return False
                if not switch and current_level and current_level[-1] >= node.val:
                    return False
                current_level.append(node.val)

            switch = not switch

        return True