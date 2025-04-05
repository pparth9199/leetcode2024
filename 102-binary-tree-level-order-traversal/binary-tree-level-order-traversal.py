# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nextLevel = deque([root])
        res=[]

        while nextLevel:
            current = nextLevel
            nextLevel = deque()
            current_nodes=[]
            while current:
                node = current.popleft()
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                current_nodes.append(node.val)
            res.append(current_nodes)
        return res