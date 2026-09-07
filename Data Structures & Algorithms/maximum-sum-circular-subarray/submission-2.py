class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum = float('inf')
        totalSum = 0
        currSum = 0
        for n in nums:
            currSum = min(currSum+n,n)
            minSum = min(minSum,currSum)
            totalSum += n

        currSum = 0
        maxSum = float('-inf')
        for n in nums:
            currSum = max(currSum+n,n)
            maxSum = max(maxSum,currSum)

        
        remain = totalSum - minSum

        if maxSum>remain or maxSum < 0:
            return maxSum
        else:
            return remain