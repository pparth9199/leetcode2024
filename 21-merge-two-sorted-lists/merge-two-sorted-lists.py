# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(-1)

        prev = mergedList

        while list1 and list2:
            if list1.val<=list2.val:
                prev.next = ListNode(list1.val)
                prev = prev.next
                list1 = list1.next
            else:
                prev.next = ListNode(list2.val)
                prev = prev.next
                list2 = list2.next

        if list1:
            prev.next = list1
        if list2:
            prev.next = list2

        return mergedList.next