class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        total = 0
        cnt = 0
        for num in nums:
            prefixSum[total] += 1
            total += num
            cnt += prefixSum[total-k]

        return cnt