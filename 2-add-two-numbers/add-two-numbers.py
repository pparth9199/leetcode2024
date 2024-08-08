# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summ=ListNode()
        res = summ
        carry=-1
        while l1 or l2:
            nodeSum=0
            if carry >0 and l1 and l2:
                nodeSum =l1.val+l2.val+carry
                carry=0
            elif carry>0 and l1:
                nodeSum = l1.val+carry
                carry=0
            elif carry>0 and l2:
                nodeSum = l2.val+carry
                carry=0
            else:
                if not l1:
                    nodeSum=l2.val
                elif not l2:
                    nodeSum = l1.val
                else:
                    nodeSum = l1.val+l2.val
            if nodeSum>9:
                carry=nodeSum//10
                nodeSum=nodeSum%10
            temp = ListNode(nodeSum)
            summ.next = temp
            summ=summ.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            
        if carry>0:
            temp = ListNode(carry)
            summ.next = temp
            
        
            
            
        return(res.next)
            