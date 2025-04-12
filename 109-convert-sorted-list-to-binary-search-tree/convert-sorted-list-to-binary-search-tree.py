# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getMiddle(head):
            fast = head
            slow = head
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow=slow.next
            if prev:
                prev.next=None
            return slow


        def FormTree(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
            
            mid = getMiddle(head)
            root = TreeNode(mid.val)
            root.right = FormTree(mid.next)
            mid.next = None
            root.left = FormTree(head)

            return root

        return FormTree(head)
        