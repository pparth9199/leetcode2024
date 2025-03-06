# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen=set()
        
        # while head is not None:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head=head.next
            
        # return False
    
        # space O(1) Solution 2
        if head is None:
                return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
