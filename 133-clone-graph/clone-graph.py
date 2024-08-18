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
        visited = {}
        def dfs(root):
            if not root:
                return root
            if root in visited:
                return visited[root]
            clone = Node(root.val,[])
            visited[root] = clone
            if node.neighbors:
                clone.neighbors = [dfs(n) for n in root.neighbors]

            return clone

        return dfs(node)