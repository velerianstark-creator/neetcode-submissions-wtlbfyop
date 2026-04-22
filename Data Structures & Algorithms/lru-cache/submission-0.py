class LRUCache:

    def __init__(self, capacity = 0):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert_to_head(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                removed_node = self.tail.prev
                self.remove(removed_node)
                del self.cache[removed_node.key]
            node = Node(key, value)
            self.insert_to_head(node)
            self.cache[key] = node
    
    def insert_to_head(self, node: Node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
