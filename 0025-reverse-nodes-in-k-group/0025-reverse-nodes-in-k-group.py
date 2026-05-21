# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        root = None # Could do head if k could be more than n

        pprev, prev = None, None
        n1, n2 = prev, head
        pprev, prev, head = prev, head, head.next
        k -= 1
        while head:
            for i in range(k):
                if head is None:
                    break
                pprev, prev, head = prev, head, head.next
                prev.next = pprev
            else:
                if n1 is None:
                    root = prev
                else:
                    n1.next = prev
                n2.next = head
                n1, n2 = n2, head
                if head:
                    pprev, prev, head = prev, head, head.next
                #break
                continue
            # Leftover re-reverse:
            n2.next = None
            n1.next = n2
            head = pprev
            pprev = None
            prev.next = None
            for j in range(i-1):
                pprev, prev, head = prev, head, head.next
                prev.next = pprev
            n2.next = prev
            break
        return root

            

