# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=set()
        def parse(root,path):

            if not root:
                return

            left = parse(root.left,path+"->"+str(root.val))
            right = parse(root.right,path+"->"+str(root.val))
            if not (root.right or root.left) :
                res.add(f'{path}->{root.val}')
            print(res)
            return res
        parse(root,'')
        return [r[2:] for r in list(res)]