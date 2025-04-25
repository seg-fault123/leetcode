# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            current1=head
            if current1 is None:
                return head
            current2=current1.next
            while current2:
                temp=current2.next
                current2.next = current1
                current1= current2
                current2=temp
            head.next=None
            return current1

        def merge(list1, list2):
            head = ListNode()
            current1= list1
            current2=list2
            current3=head
            choose_1=True
            while current1 and current2:
                if choose_1:
                    current3.next = current1
                    current1=current1.next
                else:
                    current3.next=current2
                    current2=current2.next
                current3=current3.next
                choose_1 = not choose_1
            if not current1:
                current3.next = current2
            else:
                current3.next = current1
            return head.next

        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        second=slow.next
        slow.next=None
        second = reverse(second)
        result=merge(head, second)
        return result
