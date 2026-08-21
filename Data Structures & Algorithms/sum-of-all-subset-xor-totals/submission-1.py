class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = [0]
        def solve(i,xor):
            if i == len(nums):
                result[0] += xor
                return

            solve(i+1,xor^nums[i])
            solve(i+1,xor)

        solve(0,0)
        return result[0]

