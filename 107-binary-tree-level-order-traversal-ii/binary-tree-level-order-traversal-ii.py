# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        
        queue = deque([root])
        res =[]

        while queue:
            curr = queue
            queue = deque()
            current_level = []

            while curr:
                node = curr.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level.append(node.val)
            res.append(current_level)

        return res[::-1]
                

        