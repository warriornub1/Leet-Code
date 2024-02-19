class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0)
        self.right = Node(0)
        self.right.next = self.left
        self.left.prev = self.right
    
    def insert(self, Node):
        temp = self.right.next
        self.right.next = Node
        Node.next = temp
        temp.prev = Node
        Node.prev = self.right
    
    def remove(self, Node):
        pre, nxt = Node.prev, Node.next
        nxt.next, pre.next = pre, nxt
        
    
    def get(self, key):
        if key in self.cache():
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key]
        return -1
    
    def put(self, key, val):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(val)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def printAll(self):
        temp = self.right
        while temp:
            print(temp.val)
            temp = temp.next


lRUCache = LRUCache(2)
lRUCache.insert(Node(3))
#lRUCache.printAll()
lRUCache.insert(Node(4))
lRUCache.printAll()