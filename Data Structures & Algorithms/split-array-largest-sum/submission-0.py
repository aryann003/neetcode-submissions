class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left+right)//2
            current_sum = 0
            subarr = 1
            for n in nums:
                current_sum += n
                if current_sum > mid:
                    subarr += 1
                    current_sum = n
            if subarr <=k:
                right = mid
            else:
                left = mid+1
        return left