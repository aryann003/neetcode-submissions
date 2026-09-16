class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = 0
        n = len(nums)
        for i in range(0,n+1):
            xorr = xorr ^ i

        for i in range(0,len(nums)):
            xorr = xorr ^ nums[i]
        
        return xorr