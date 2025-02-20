# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = ListNode()
        p3 = head

        while (p1 and p2):
            if p1.val == p2.val:
                p3.next = ListNode(p1.val)
                p3=p3.next
                p3.next= ListNode(p2.val)
                p3=p3.next
                p1 = p1.next
                p2 = p2.next
            elif p1.val < p2.val:
                p3.next = ListNode(p1.val)
                p1 = p1.next
                p3 = p3.next
            elif p2.val < p1.val:
                p3.next = ListNode(p2.val)
                p2 = p2.next
                p3 = p3.next
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2
        head = head.next
        return head
                
