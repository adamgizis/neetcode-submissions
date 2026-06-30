# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        it = head
        while it is not None:
            stack.append(it)
            it = it.next
        
        count = len(stack) // 2
        it = head
        while count > 0:
            node = stack.pop()
           
            n = it.next
            it.next = node
            node.next = n
            it = n
            
            count-=1
        it.next = None

