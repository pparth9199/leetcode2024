# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        orderlist = defaultdict(list)
        nextLevel = deque([(root, 0)])

        while nextLevel: 
            node, col = nextLevel.popleft()
            orderlist[col].append(node.val)

            if node.left:
                nextLevel.append((node.left,col-1))
            if node.right:
                nextLevel.append((node.right,col+1))
        res = []

        for i in sorted(orderlist):
            res.append(orderlist[i])
        return res
        
        ans = []
        for i in sorted(orderlist):
            ans.append(orderlist[i])
        return ans
        