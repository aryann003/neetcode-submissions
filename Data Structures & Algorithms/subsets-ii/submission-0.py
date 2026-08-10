class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def solve(nums, ans, index):
            if index == len(nums):
                result.append(list(ans))
                return

            ans.append(nums[index])
            solve(nums,ans,index+1)
            ans.pop()

            index += 1
            while index < len(nums) and nums[index] == nums[index-1]:
                index += 1
            solve(nums,ans,index)
        ans = []
        solve(nums,ans,0)

        return result

        
