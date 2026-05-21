# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        root = head
        left -= 1
        pprev, prev = None, None
        n1, n2 = None, None
        for i in range(right):
            if i == left:
                n1, n2 = prev, head
            pprev = prev
            prev = head
            head = head.next
            if left < i:
                prev.next = pprev
        
        if n1:
            n1.next = prev
        n2.next = head

        return root if left > 0 else prev
