# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        dummy = ListNode(-1)
        temp3 = dummy
        carry = 0
        while temp1 and temp2:
            sum = carry
            sum += temp1.val + temp2.val
            temp = sum % 10
            temp3.next = ListNode(temp)
            carry = sum // 10
            temp1 = temp1.next
            temp2 = temp2.next
            temp3 = temp3.next
        while temp1:
            temp = temp1.val + carry
            temp3.next = ListNode(temp % 10)
            carry = temp // 10
            temp1 = temp1.next
            temp3 = temp3.next
        while temp2:
            temp = temp2.val + carry
            temp3.next = ListNode(temp % 10)
            carry = temp // 10
            temp2 = temp2.next
            temp3 = temp3.next
        if carry:
            temp3.next = ListNode(carry)
        return dummy.next
