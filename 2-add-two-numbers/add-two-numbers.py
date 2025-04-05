# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # s1=s2=""
        # while l1 or l2:
        #     if l1:
        #         s1+=str(l1.val)
        #         l1=l1.next
        #     if l2:
        #         s2+=str(l2.val)
        #         l2 = l2.next
        # summ = str(int(s1[::-1])+int(s2[::-1]))
        # listSum = list(summ)
        # head = ListNode(int(listSum[-1]))
        # iterator = head
        # for i in range(len(listSum)-2,-1,-1):
        #     iterator.next = ListNode(int(listSum[i]))
        #     iterator = iterator.next
        # return head


        dummy = ListNode(0)
        curr = dummy
        carry=0

        while l1 or l2 or carry!=0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            summ = l1Val+l2Val+carry

            carry = summ//10
            newNode = ListNode(summ%10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next