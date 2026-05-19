"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        seen = {None: None}
        root = ListNode()
        nhead = root
        while head:
            if head in seen:
                nhead.next = seen[head]
            else:
                nhead.next = ListNode(head.val)
                seen[head] = nhead.next
            nhead = nhead.next
            if head.random in seen:
                nhead.random = seen[head.random]
            else:
                nhead.random = ListNode(head.random.val)
                seen[head.random] = nhead.random
            head = head.next
        
        return root.next