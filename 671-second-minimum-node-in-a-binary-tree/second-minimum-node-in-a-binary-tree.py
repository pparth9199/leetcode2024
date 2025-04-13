# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        heap = set()
        def dfs(root):
            nonlocal heap
            if not root:
                return
            heap.add(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(heap)
        heap=list(heap)
        heapq.heapify(heap)
        
        heapq.heappop(heap)

        return heapq.heappop(heap) if len(heap)>=1 else -1