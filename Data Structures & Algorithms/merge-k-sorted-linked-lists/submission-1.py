# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        for l in lists:
            while l is not None:
                heapq.heappush(heap, l.val)
                l = l.next

        s = ListNode()
        curr = s
        while len(heap) > 0:
            smallest = heapq.heappop(heap)
            curr.next = ListNode(smallest, None)
            curr = curr.next
        
        s = s.next
        return s
                    
            
                