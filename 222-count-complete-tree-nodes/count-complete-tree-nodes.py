# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([(root)])
        prev = None
        count=1
        while queue:
            next_level = queue
            queue=deque()
            while next_level:
                node = next_level.popleft()
                if prev!=None:
                    count+=1
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return count
                
