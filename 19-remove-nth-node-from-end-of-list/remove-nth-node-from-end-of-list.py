# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        res=head
        length=0
        while head:
            length+=1
            head=head.next
        nth = length-n
        print(nth)
        if length==1:
            return ListNode().next
        if nth==0:
            return temp.next
        for i in range(0,nth-1):
            temp=temp.next
            
        
        temp.next = temp.next.next
        
        return res
            