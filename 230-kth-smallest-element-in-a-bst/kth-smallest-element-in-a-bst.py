# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap=[]
        def parse(root):
            if not root:
                return 
            left = parse(root.left)
            right = parse(root.right)
            heapq.heappush(heap,root.val)
        parse(root)

        while k-1:
            heapq.heappop(heap)
            k-=1
        return heap[0]