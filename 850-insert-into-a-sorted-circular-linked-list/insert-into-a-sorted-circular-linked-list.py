"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        prev, curr = head, head.next
        inserted = False

        while True:
            if prev.val <= insertVal <= curr.val:
                inserted = True
            elif prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                inserted = True
            if inserted:
                new_node = Node(insertVal)
                prev.next = new_node
                new_node.next = curr
                return head

            prev, curr = curr, curr.next
            if prev == head:  
                break

        new_node = Node(insertVal)
        prev.next = new_node
        new_node.next = curr
        return head