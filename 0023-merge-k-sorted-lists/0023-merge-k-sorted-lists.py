# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        i = 0
        for head in lists:
            if head is None:
                continue
            heapq.heappush(heap, (head.val, i, head))
            i += 1
        root = ListNode()
        head = root
        while heap:
            val, _, node = heapq.heappop(heap)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                i += 1
        
        return root.next