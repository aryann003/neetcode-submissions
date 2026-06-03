class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        min_length = float('inf')
        sum = 0
        while end < len(nums):
            sum += nums[end]

            while sum >= target:
                length = end-start+1
                min_length = min(min_length,length)
                sum -= nums[start]
                start += 1
            end += 1
            

        if min_length == float('inf'):
            return 0
        else:
            return min_length

