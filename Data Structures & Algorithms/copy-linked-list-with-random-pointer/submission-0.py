"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}
        m[None] = None

        it = head

        nh = None
        pc = None
    
        while it:
            #create a copy of it
            node = Node(it.val, None, None)
           # map it for the randome
            m[it] = node
           
            if pc:
                pc.next = node
            else:
                nh = node
            
            pc = node

            # iterate to the next
            it = it.next

        # add the random
        it = head
        nl = nh
        while it:
            nl.random = m[it.random]
            it = it.next
            nl = nl.next
    
        return nh