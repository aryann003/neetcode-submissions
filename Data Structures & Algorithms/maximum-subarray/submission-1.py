class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        currSum = 0
        maxSum = float('-inf')
        for n in nums:
            currSum = max(currSum+n , n)
            maxSum = max(maxSum,currSum)
        return maxSum