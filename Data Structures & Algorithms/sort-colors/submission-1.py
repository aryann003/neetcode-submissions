class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        second = len(nums)-1
        third = 0

        while third <= second:
            if nums[third] == 0:
                nums[first],nums[third] = nums[third],nums[first]
                first += 1
                third += 1
            elif nums[third] == 2:
                nums[second],nums[third] = nums[third],nums[second]
                second -= 1
            else:
                third += 1
        