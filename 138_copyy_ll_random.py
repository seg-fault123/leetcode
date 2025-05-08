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
        if not head:
            return

        current = head
        # copy of each node is assigned as the next of the original node.
        # So if the list is A -> B -> C, it gets changed to A->A'->B->B'->C->C'
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next
        
        current = head
        new_head = current.next
        # the correct connection of the new list are made
        while current:
            original_next = current.next.next
            original_random = current.random
            copied = current.next
            
            if original_next:
                copied.next = original_next.next
            else:
                copied_next = None
            if original_random:
                copied.random = original_random.next
            else:
                copied.random = None

            current = original_next
        
        return new_head
