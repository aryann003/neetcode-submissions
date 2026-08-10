class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(nums,ans,used):
            if len(ans) == len(nums):
                result.append(list(ans))
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                ans.append(nums[i])

                solve(nums,ans,used)

                ans.pop()
                used[i] = False

                
        ans = []
        used =[False] * len(nums)
        solve(nums,ans,used)
        return result