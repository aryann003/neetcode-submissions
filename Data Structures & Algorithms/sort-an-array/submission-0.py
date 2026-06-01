class Solution:

    def merge(self, nums1 : List[int], nums2 : List[int])-> List[int]:
        result = []
        i = 0;
        j = 0;
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        return result
    
    def mergeSort(self, nums:List[int])->List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left,right)


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)