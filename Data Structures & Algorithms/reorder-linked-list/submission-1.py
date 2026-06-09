# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, node):
        if node is None:
            return None
        newHead = node
        if node.next:
            newHead = self.reverseList(node.next)
            node.next.next = node
        node.next = None
        return newHead

    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 - Find the middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2 - Reverse second half
        head2 = self.reverseList(slow.next)
        slow.next = None

        # 3 - Merge the two halves
        first, second = head, head2
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        