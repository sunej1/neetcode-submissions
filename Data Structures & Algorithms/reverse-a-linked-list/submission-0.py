# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        reversed = ListNode(0, None)
        curr1 = reversed
        while head is not None:
            curr1.next = ListNode(head.val, curr1.next)
            head = head.next
        
        return reversed.next
            
