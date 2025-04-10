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
    def connect(self, root: 'Node') -> 'Node':
        queue=deque([(root)])
        if not root:
            return root
        while queue:
            level = queue
            queue = deque()
            current_level=[]
            while level:
                node = level.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if current_level:
                    current_level[-1].next = node
                current_level.append(node)
            
        return root