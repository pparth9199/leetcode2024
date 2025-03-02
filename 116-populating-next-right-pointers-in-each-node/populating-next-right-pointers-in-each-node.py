"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque([root])
        while queue:
            n = len(queue)
            leftmost = None
            for i in range(n):
                node = queue.popleft()
                if leftmost:
                    leftmost.next = node
                leftmost = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

