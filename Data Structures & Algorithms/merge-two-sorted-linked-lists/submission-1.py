# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        curr = dummyNode
        t1 = list1
        t2 = list2
        while t1 or t2:
            if not t2:
                curr.next = ListNode(t1.val)
                t1 = t1.next
                curr = curr.next
            elif not t1:
                curr.next = ListNode(t2.val)
                t2 = t2.next
                curr = curr.next
            elif t1.val == t2.val:
                curr.next = ListNode(t1.val)
                t1 = t1.next
                curr = curr.next
                curr.next = ListNode(t2.val)
                t2 = t2.next
                curr = curr.next
            elif t1.val < t2.val:
                curr.next = ListNode(t1.val)
                t1 = t1.next
                curr = curr.next
            else:
                curr.next = ListNode(t2.val)
                t2 = t2.next
                curr = curr.next

        return dummyNode.next
        