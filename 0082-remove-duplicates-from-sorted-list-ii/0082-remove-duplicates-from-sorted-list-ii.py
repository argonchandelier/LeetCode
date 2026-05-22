# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = None
        prev = None
        last = None
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head.next = head.next.next
                head = head.next
                if prev:
                    prev.next = head
            else:
                if prev is None:
                    root = head
                prev, head = head, head.next
        return root                    
