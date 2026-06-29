# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2

        temphead = ListNode()
        it = temphead
        
        while h1 is not None and h2 is not None:
            m = h1 if h1.val < h2.val else h2
            if m == h1:
                h1 = h1.next
            else:
                h2 = h2.next
            it.next = m
            it = it.next
        if h1:
            it.next = h1
        if h2:
            it.next = h2
        return temphead.next
