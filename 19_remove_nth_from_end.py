# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we will maintain a gap of n-1 between start and end.
        # then we will update the proceed the start and end pointers one by one until the end pointer is the last node.
        # in this position, the start pointer needs to be deleted
        parent = None
        start = head
        end = head
        for _ in range(n-1):
            end = end.next
        
        while end.next is not None:
            parent = start
            start = start.next
            end = end.next
        
        if parent:
            parent.next = start.next
            parent = head
        else:
            parent = start.next
        
        return parent

