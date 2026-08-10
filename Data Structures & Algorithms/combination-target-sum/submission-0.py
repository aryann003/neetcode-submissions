class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def solve(nums,index,target,ans):
            if target == 0:
                return result.append(list(ans))
            if index == len(nums) or target < 0:
                return 
            #take

            ans.append(nums[index]) 
            solve(nums,index,target-nums[index],ans)
            ans.pop()
            solve(nums,index+1,target,ans)


        solve(nums,0,target,[])
        return result


        