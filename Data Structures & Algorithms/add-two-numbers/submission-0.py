# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        it1 = l1
        it2 = l2
        h1 = ListNode()
        head = h1
        carry = 0 
        while it1 or it2:
            v1 = it1.val if it1 else 0 
            v2 = it2.val if it2 else 0 
            v = (carry + v1 + v2)
            carry = v // 10
            v = v % 10
            h1.val  = v
            it1 = it1.next if it1 else None
            it2 = it2.next if it2 else None
            if it1 or it2:
                n = ListNode()
                h1.next = n
                h1 = n

        if carry > 0:
            n = ListNode(carry)
            h1.next = n

        



        return head



