# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        temp2 = head.next

        while temp2:

            gcdd = math.gcd(temp1.val,temp2.val)

            node = ListNode(gcdd)

            temp1.next = node
            node.next = temp2
            temp1 = temp2
            temp2 = temp2.next

        return head
        
         