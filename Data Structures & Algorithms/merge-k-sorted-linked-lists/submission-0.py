class Solution:
    def merge(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next

    def mergeKLists(self, lists):
        if not lists:
            return None

        def mergeSort(start, end):
            if start == end:
                return lists[start]

            mid = (start + end) // 2

            left = mergeSort(start, mid)
            right = mergeSort(mid + 1, end)

            return self.merge(left, right)

        return mergeSort(0, len(lists) - 1)