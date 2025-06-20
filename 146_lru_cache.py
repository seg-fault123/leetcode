class LRUCache:
    class Node:
        def __init__(self, val, prev=None, next=None, key= None):
            self.val = val
            self.prev = prev
            self.next = next
            self.key = key # will be needed for determining the key for deleting from the key_node dict when this node is the LRU node
    

    # LRU node is the last node in the linked list,
    # key_node dict gives the node corresponding to the key value
    # the recent node is brought to the front of the list
    def __init__(self, capacity: int):
        self.head = self.Node(None)
        self.tail = self.Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.key_node = {}

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self.make_first(node)
        # self.print_ll()
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            self.make_first(node)
            node.val = value
            return

        elif self.capacity == self.size:
            lru_node = self.tail.prev
            lru_node.prev.next = lru_node.next
            lru_node.next.prev = lru_node.prev
            del self.key_node[lru_node.key]
            self.size -= 1
        
        new_node = self.Node(value, None, None, key)
        self.key_node[key] = new_node
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next = new_node
        new_node.next.prev = new_node
        self.size+=1


    def make_first(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def print_ll(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr=curr.next
        print()
        curr = self.tail
        while curr:
            print(curr.val, end=' ')
            curr = curr.prev
        print()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
