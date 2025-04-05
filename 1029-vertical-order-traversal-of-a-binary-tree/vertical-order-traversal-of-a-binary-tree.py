# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        orderList = defaultdict(list)
        queue = deque([(root, (0, 0))])

        while queue:
            node, (row, col) = queue.popleft()
            orderList[(row, col)].append(node.val)

            if node.left:
                queue.append((node.left, (row + 1, col - 1)))
            if node.right:
                queue.append((node.right, (row + 1, col + 1)))

        # Sort keys first by col, then row, then value (if needed)
        sorted_keys = sorted(orderList.keys(), key=lambda x: (x[1], x[0]))

        # Group by column
        cache = defaultdict(list)
        for key in sorted_keys:
            col = key[1]
            for val in sorted(orderList[key]):
                cache[col].append(val)

        # Final 2D list (sorted by column)
        return [cache[col] for col in sorted(cache)]
        
        