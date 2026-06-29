# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        it = head 
        
        while it is not None:
            t = it
            it = it.next
            t.next = prev
            prev = t

        if prev:
            return prev
        return head
        
        
