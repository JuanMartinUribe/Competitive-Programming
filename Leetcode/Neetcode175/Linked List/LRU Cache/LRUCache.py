class Node:
    def __init__(self,val=None,nxt=None,prev=None):
        self.val=val
        self.nxt=nxt
        self.prev=prev
class LinkedList:
    def __init__(self,l=0,head=None,tail=None):
        self.l=l
        self.head = head
        self.tail = tail
    def add(self,node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.head.nxt = node
            node.prev = self.head
            self.head = node
        self.l+=1
    def remove(self,node):
        if self.head==node and self.tail==node:
            self.head=None
            self.tail = None
        else:
            if node==self.tail:
                self.tail = node.nxt
                self.tail.prev = None
            elif node==self.head:
                self.head = node.prev
                self.head.nxt = None
            elif node.prev and node.nxt:
                node.prev.nxt = node.nxt
                node.nxt.prev = node.prev
            node.nxt = None
            node.prev = None
        self.l-=1
class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.ll = LinkedList()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.lookup and self.lookup[key].val!=-1:
            self.ll.remove(self.lookup[key])
            self.ll.add(self.lookup[key])
            return self.lookup[key].val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.lookup and self.lookup[key].val!=-1:
            node = self.lookup[key]
            self.ll.remove(node)
            self.ll.add(node)
            node.val=value
        else:
            if self.ll.l==self.capacity:
                self.ll.tail.val=-1
                self.ll.remove(self.ll.tail)
            self.lookup[key] = Node(value)
            self.ll.add(self.lookup[key])
            print(self.ll.tail.val,self.ll.head.val,key)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)