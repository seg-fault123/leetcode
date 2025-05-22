# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current_index = 0
        current = ListNode(0, head)
        dummy = current # for handling edge cases smoothly

        # go to the parent of left
        while current_index < left-1:
            current_index += 1
            current = current.next
        
        # store this (parent of left)
        dummy2 = current

        # reverse the list starting from left
        current = current.next
        coming = current.next
        current_index += 1
        # coming pointer's next pointer needs to be updated, current's next has been updated (except the first one, which will be done later)
        while current_index < right:
            temp = coming.next
            coming.next = current
            current = coming
            coming = temp
            current_index += 1
        
        #update the next pointers of the first node (left) and dummy2.next to point to right, which will become first after reversing
        left_node = dummy2.next
        left_node.next = coming
        dummy2.next = current

        return dummy.next

