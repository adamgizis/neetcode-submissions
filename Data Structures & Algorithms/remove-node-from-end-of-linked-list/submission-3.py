# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        it = head
        count = 0

        while count != n:
            it = it.next
            count +=1
        prev = None
        nth = head
        
        while it is not None:
            prev = nth
            nth = nth.next
            it = it.next


        if nth == head:
            head = head.next
            return head

        prev.next = nth.next

        return head
