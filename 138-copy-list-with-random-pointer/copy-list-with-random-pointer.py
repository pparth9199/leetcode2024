"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        cache = {None:None}
        while temp:
            copy = Node(temp.val)
            cache[temp] =copy
            temp=temp.next
            
        temp=head
        while temp:
            copy = cache[temp]
            copy.next = cache[temp.next]
            copy.random = cache[temp.random]
            temp = temp.next
        return cache[head]
        