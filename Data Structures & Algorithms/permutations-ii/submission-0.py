class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def solve(nums,flag, ans):
            if len(nums) == len(ans):
                result.add(tuple(ans))
                return 

            for i in range(len(nums)):
                if flag[i]:
                    continue
                ans.append(nums[i])
                flag[i] = True
                solve(nums,flag,ans)
                ans.pop()
                flag[i] = False

        flag = [False] * len(nums)
        ans = []
        solve(nums,flag,ans)

        return [list(x) for x in result]