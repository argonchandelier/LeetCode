# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n1, n2 = head, head
        while n2 is not None and n2.next is not None:
            n1, n2 = n1.next, n2.next.next
            if n1 == n2:
                return True
        return False