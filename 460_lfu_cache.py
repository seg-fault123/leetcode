# https://leetcode.com/problems/lfu-cache/solutions/207673/python-concise-solution-detailed-explanation-two-dict-doubly-linked-list/
class LFUCache:
    class Node:
        def __init__(self, value, key):
            self.val = value
            self.key = key
            self.freq = 1
            self.next = None
            self.prev = None
    
    class DLL:
        def __init__(self):
            self.head = LFUCache.Node(None, None)
            self.tail = LFUCache.Node(None, None)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0
        
        def add(self, node):
            node.next = self.head.next
            node.prev = self.head

            self.head.next = node
            node.next.prev = node
            self.size += 1

        def delete(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        
        def print_ll(self):
            curr = self.head
            while curr:
                print(curr.val, end = " ")
                curr = curr.next
            print()
            curr = self.tail
            while curr:
                print(curr.val, end=" ")
                curr = curr.prev
            print()


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 1

        self.key_node = {}
        self.count_dll = {}

    def print_ds(self):
        for key, value in self.count_dll.items():
            print(key)
            value.print_ll()
            print('================')

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        
        node = self.key_node[key]
        freq = node.freq
        new_freq = freq+1
        self.count_dll[freq].delete(node)
        if new_freq not in self.count_dll:
            self.count_dll[new_freq] = self.DLL()
        self.count_dll[new_freq].add(node)

        if self.count_dll[freq].size == 0:
            if self.min_freq == freq:
                self.min_freq = new_freq
            del self.count_dll[freq]
        
        node.freq = new_freq
        # self.print_ds()
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self.get(key)
            return
        
        new_node = self.Node(value, key)
        self.key_node[key] = new_node
        if self.size == self.capacity:
            lfu_node = self.count_dll[self.min_freq].tail.prev
            self.count_dll[self.min_freq].delete(lfu_node)
            del self.key_node[lfu_node.key]
            self.size -= 1
        
        if 1 not in self.count_dll:
            self.count_dll[1] = self.DLL()
        self.count_dll[1].add(new_node)
        if self.count_dll[self.min_freq].size == 0:
            del self.count_dll[self.min_freq]
        self.min_freq = 1
        self.size += 1
        # self.print_ds()



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
