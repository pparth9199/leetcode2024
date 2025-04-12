# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return (0,0)
            sum_left,num_of_nodes_left = dfs(root.left)
            sum_right, num_of_nodes_right = dfs(root.right)
            current_sum=root.val+sum_left+sum_right
            num_of_nodes_at_level = num_of_nodes_left+num_of_nodes_right+1
            avg = current_sum//num_of_nodes_at_level
            if avg==root.val:
                count+=1
            return (current_sum,num_of_nodes_at_level)

        dfs(root)
        return count