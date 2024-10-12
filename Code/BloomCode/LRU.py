class Node:
    def __init__(self,key=None, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}
        self.cap = capacity

    def add(self, node):
        leftNode = self.right.prev
        leftNode.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = leftNode

    def remove(self, node):
        leftNode = node.prev
        rightNode = node.next
        leftNode.next = rightNode
        rightNode.prev = leftNode
    
    def get(self, key: int) -> int:
        if(key in self.map):
            getNode = self.map[key]
            self.remove(getNode)
            self.add(getNode)
            return getNode.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.map):
            node = self.map[key]
            self.remove(node)

        newNode = Node(key,value)
        self.add(newNode)
        self.map[key] = newNode

        if(len(self.map)>self.cap):
            remNode = self.left.next
            print('node to remove',remNode.key)
            del self.map[remNode.key]
            nxtNode = remNode.next
            self.left.next = nxtNode
            nxtNode.prev = self.left
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)