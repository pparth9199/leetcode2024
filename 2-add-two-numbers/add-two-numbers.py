# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        num1 = []
        num2 = []
        
        p1 = l1
        while p1:
            num1.append(p1.val)
            p1 = p1.next
        
        p2 = l2
        while p2:
            num2.append(p2.val)
            p2 = p2.next
        num1[::] = num1[::-1]
        num2[::] = num2[::-1]

        n1 = 0
        n2 = 0
       
        for i in range(len(num1)):
            zero = len(num1) - i - 1
            n1 = n1 + (num1[i] * (10**zero))
       
        for i in range(len(num2)):
            zero = len(num2) - i - 1
            n2 = n2 + (num2[i] * (10**zero))

        s = n1 + n2
        
        l = list(map(int, str(s)))
        l[::] = l[::-1]
        
        head = ListNode()
        p = head
        
        for i in range(len(l)-1):
            p.val = l[i]
            p.next = ListNode()
            p = p.next
        p.val = l[-1]
        return head
