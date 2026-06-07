# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head2, head3 = head, head
        while head3.next and head3.next.next:
            head2 = head2.next
            head3 = head3.next.next

        head2n = head2.next
        head2.next = None
        head2 = head2n

        head, head2 = self.sortList(head), self.sortList(head2)
        root = ListNode()
        cnode = root
        while head and head2:
            if head.val < head2.val:
                cnode.next = head
                head = head.next
            else:
                cnode.next = head2
                head2 = head2.next
            cnode = cnode.next
        cnode.next = head if head else head2

        return root.next
                


        