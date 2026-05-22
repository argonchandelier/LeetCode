# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        n = 0
        root = head
        while head.next:
            head = head.next
            n += 1
        n += 1
        k %= n
        if k == 0:
            return root

        n1, n2 = root, root
        for i in range(n-k-1):
            n2 = n2.next
        root, head.next, n2.next = n2.next, root, None
        return root
        