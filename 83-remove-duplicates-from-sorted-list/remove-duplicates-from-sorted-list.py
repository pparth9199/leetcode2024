# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = ListNode(head.val,None)
        res = prev
        head = head.next
        while head:
            if head.val==prev.val:
                head=head.next
            else:
                prev.next = ListNode(head.val,None)
                prev =prev.next
                head=head.next

        return res

