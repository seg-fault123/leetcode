import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use a priority queue to maintain least of the current elements in the k lists
        result = ListNode()
        curr = result

        heap  = []
        for i, head in enumerate(lists):
            if head:
                # we store the index from the element came, as it will be used to update the pointer list at that index
                heap.append((head.val, i))
                lists[i] = head.next

        heapq.heapify(heap)
        while heap:
            value, index = heapq.heappop(heap)
            curr.next = ListNode(value)
            curr = curr.next
            # if lists[index] is None, no need to add it
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next
        
        return result.next
            

