class Node:
    def __init__(self, key, val, nex=None, prev=None):
        self.key = key 
        self.val = val
        self.next = nex
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.count = 0
        self.head = None
        self.tail = None

    def __remove_node(self, node):
        # clean up the global pointers
        if node == self.tail:
            self.tail = node.prev
        if node == self.head:

            self.head = node.next
            
        p = node.prev
        n = node.next
        if p: 
            p.next = n
        if n:
            n.prev = p
        node.next = None
        node.prev = None
    
    def __add_to_front(self,node):
        if not self.head:
            self.head = node
            self.tail = node
            return

        h = self.head

        h.prev = node
        node.next = h
        node.prev = None

        self.head = node


    def __remove_from_tail(self):
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        p = self.tail.prev
        if p:
            p.next = None
            self.tail = p
        else:
            self.tail = None


    def get(self, key: int) -> int:
        node = self.store.get(key, -1)
        # add to front of the cache
        if node == -1:
            return node
        
        #node equals key: node, node has node.val
        # remove node from list attach the prev to the next
        self.__remove_node(node)
        self.__add_to_front(node)

        return node.val
        


    def put(self, key: int, value: int) -> None:
        node = Node(key,value)

        if key in self.store:
            n = self.store[key]
            self.__remove_node(n)
            self.count-=1
        elif self.count + 1 > self.cap:
            if self.tail:
                self.store.pop(self.tail.key)
            self.__remove_from_tail()
            self.count-=1
        
        self.store[key] = node
        self.__add_to_front(node)
        self.count+=1

        return 


        
