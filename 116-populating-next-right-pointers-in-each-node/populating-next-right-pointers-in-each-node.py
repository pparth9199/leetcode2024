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
        temp=root
        if not root:
            return temp
        q=deque([root])
        while q:
            level=[]
            size=len(q)
            for i in range(size):
                current = q.popleft()
                level.append(current.val)
                if q and len(level)<size: current.next=q[0]
                else: current.next=None
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

        return temp