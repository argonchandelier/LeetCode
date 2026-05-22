# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lroot, rroot = ListNode(), ListNode()
        lhead, rhead = lroot, rroot
        while head:
            prev, head = head, head.next
            if prev.val < x:
                lhead.next = prev
                lhead = lhead.next
            else:
                rhead.next = prev
                rhead = rhead.next
        lhead.next = rroot.next
        rhead.next = None
        return lroot.next
