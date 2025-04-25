# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1=list1
        current2=list2
    
        head = ListNode() ## use the first node in the list as a dummy
        current3=head
        while current1 and current2:
            if  current1.val < current2.val:
                current3.next = current1
                current1=current1.next
            else:
                current3.next = current2
                current2 = current2.next
            current3 = current3.next
        if current1:
            current3.next = current1
        else:
            current3.next = current2
        return head.next # since first node is a dummy, return the remaining list
    

    ## Recursion
        # if not list1:
        #     return list2
        # elif not list2:
        #     return list1
        
        # if list1.val > list2.val:
        #     list1, list2 = list2, list1
        
        # list1.next = self.mergeTwoLists(list1.next, list2)
        # return list1
