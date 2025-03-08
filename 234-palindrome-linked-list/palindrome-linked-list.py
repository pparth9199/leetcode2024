# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        checker=[]
        while head:
            checker.append(head.val)
            head = head.next
        return checker==checker[::-1]