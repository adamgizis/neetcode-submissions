# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid point
        it = head
        m = head
        p = None
        count = 0

        while it is not None:
            if count % 2 == 0:
                p = m
                m = m.next
            it = it.next
            count+=1

        # now reverse the second half
        p.next = None

        it = m
        prev = None
        while it is not None:
            t = it.next
            it.next = prev
            prev = it
            it = t

        first = head
        second = prev

        while first is not None and second is not None:

            next1 = first.next 
            next2 = second.next
            first.next = second
            second.next = next1

            first = next1
            second = next2
        

    
        



        



