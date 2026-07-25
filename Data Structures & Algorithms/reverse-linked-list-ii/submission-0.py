# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        temp = head
        head1 = None

        for i in range(1,left):
            head1 = temp
            temp = temp.next

        curr = temp
        prev = None

        for i in range(0,right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        temp.next = curr
        if not head1:
            head = prev

        else:
            head1.next = prev
        return head