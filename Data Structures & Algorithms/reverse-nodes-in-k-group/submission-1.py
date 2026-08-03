# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        for i in range(0,k):
            if not temp:
                return head
            temp = temp.next

        curr = head
        prev = None
        Next = None

        for i in range(0,k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head.next = self.reverseKGroup(curr,k)

        return prev

        