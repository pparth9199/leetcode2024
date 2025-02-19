"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        while queue:
            n = queue.popleft()
            for i in n.neighbors:
                if i not in visited:
                    visited[i] = Node(i.val, [])
                    queue.append(i)
                visited[n].neighbors.append(visited[i])
        return visited[node]
