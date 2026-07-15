"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
FIRST PASS: L1 node values do not change. But their random becomes the new L2 nodes.

New L2 nodes' value are their corresponding L1 nodes.
New L2 nodes' next are L1 nodes' random.
L1 nodes' random becomes L2 nodes. Random is saved in L2.next
Move to next L1 node.

SECOND PASS: Fix random pointers of copies


THIRD PASS: Extract copied list and restore original list
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        l1 = head

        while l1:
            l2 = Node(l1.val)
            l2.next = l1.random
            l1.random = l2
            l1 = l1.next
        
        newHead = head.random
        l1 = head
        while l1:
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None
            l1 = l1.next
        
        l1 = head
        while l1:
            l2 = l1.random
            l1.random = l1.next
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next

        return newHead


        