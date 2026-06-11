# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        curr = head
        group = head
        new_tail = None
        new_head = None

        first = True 
        while group:
            i = 0
            while group and i < k:
                group = group.next
                i+=1
            if i == k:
                while curr != group:
                    temp = curr.next
                    curr.next = prev
                    prev = curr # prev is the new head
                    curr = temp
                if first:
                    new_head = prev
                    new_tail = prev
                    first = False
                else:
                    new_tail.next = prev
                while new_tail and new_tail.next:
                    new_tail = new_tail.next
                prev = None

            else:
                if first:
                    new_head = head
                else:
                    new_tail.next = curr

        return new_head