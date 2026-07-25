"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {}
        dummy = Node(-1)
        temp1 = dummy
        temp = head

        while temp:
            tmp = Node(temp.val)
            temp1.next = tmp
            mp[temp] = tmp
            temp1 = temp1.next
            temp = temp.next

        temp = head
        temp1 = dummy.next

        while temp:
            temp1.random = mp.get(temp.random)
            temp1 = temp1.next
            temp = temp.next

        return dummy.next  