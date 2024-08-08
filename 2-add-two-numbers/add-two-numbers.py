# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summ=ListNode()
        res = summ
        carry=0
        while l1 or l2 or carry:
            one = l1.val if l1 else 0
            two = l2.val if l2 else 0
            nodeSum = one+two+carry
            carry=nodeSum//10
            nodeSum=nodeSum%10
            temp = ListNode(nodeSum)
            summ.next = temp
            summ=summ.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            
            
        
            
            
        return(res.next)
            