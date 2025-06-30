# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # def reverse_group(node, index, k):
        #     if node is None:
        #         return (index%k==1, [None, None], None)
            
        #     reverse, [start, end], tail = reverse_group(node.next, index+1, k)
        #     # print(reverse, start.val if start else None, end.val if end else None, tail.val if tail else None)
        #     if not reverse:
        #         start = node
        #         if end is None:
        #             end = node
        #     else:
        #         if end is None:
        #             start = end = node
        #         else:
        #             end.next, end = node, node
            
        #     if index%k==1:
        #         end.next = tail
        #         tail = start
        #         return True, [None, None], tail
        #     else:
        #         return reverse, [start, end], tail
        
        # if k==1:
        #     return head
        
        # _, [_, _], tail = reverse_group(head, 1, k)
        # return tail

        # get the kth node after the current node, the next node is counted as 1
        def get_kth(curr, k):
            while curr and k>0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode()
        dummy.next = head
        prev_group = dummy # end Pointer of previous group

        while True:
            # get the last node of this group
            kth_node = get_kth(prev_group, k)
            if kth_node is None:
                # no need to reverse
                return dummy.next
            
            # iterator through the group
            curr = prev_group.next
            next_group = kth_node.next
            
            # reverse the linked list from curr to kth_node
            prev = next_group
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # link the previous group to the new start of the current group
            temp = prev_group.next
            prev_group.next = kth_node
            prev_group = temp # update the previous grouo
        
        




