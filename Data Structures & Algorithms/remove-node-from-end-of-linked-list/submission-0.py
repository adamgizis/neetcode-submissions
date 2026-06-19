# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(val = 0, next = head)
        prev = dummy
        it = head

        count = 0
        while count < n:
            it = it.next
            count+=1 
        


        while it:
            prev = prev.next
            it = it.next
            count +=1    

        prev.next = prev.next.next

        if count- n == 0:
            return head.next
           

        return head



