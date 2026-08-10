class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(nums, index, ans):
            if index == len(nums):
                return result.append(list(ans))

            # take
            ans.append(nums[index])
            solve(nums,index+1,ans)

            ans.pop()

            solve(nums,index+1,ans)
        solve(nums,0,[])
        return result
        