# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def removeNth(head):
            nonlocal n
            if head is None:
                return 0
            res = removeNth(head.next)
            if res == n:
                head.next = head.next.next
            return 1 + res
        dummy = ListNode(0, head)
        removeNth(dummy)
        return dummy.next