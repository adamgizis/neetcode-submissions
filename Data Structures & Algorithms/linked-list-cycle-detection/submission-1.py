# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head.next if head and head.next else None
        slow = head if head else None
        
        while fast is not None and slow is not None:
            if fast == slow:
                return True

            fast = fast.next.next if fast.next and fast.next.next else None
            slow = slow.next if slow.next else None


            

        
        return False