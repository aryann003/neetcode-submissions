class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = []
        total = (len(nums1) + len(nums2))
        idx = total // 2
        while len(lst) < idx + 1:
            if nums1 and nums2 and nums1[0] > nums2[0]:
                lst.append(nums2.pop(0))
            elif nums1 and nums2 and nums1[0] < nums2[0]:
                lst.append(nums1.pop(0))
            elif len(nums1) == 0:
                lst.extend(nums2)
            else:
                lst.extend(nums1)

        if total % 2 != 0:
            return lst[idx]
        else:
            return (lst[idx] + lst[idx-1]) / 2