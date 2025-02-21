# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next
        arr [::] = arr [::-1]
        p = head
        i = 0
        while p:
            p.val = arr[i]
            p = p.next
            i = i + 1
        return head