class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = [0]
        def solve(i,ans):
            if i == len(nums):
                
                temp = 0
                for j in range(len(ans)):
                    temp = temp ^ ans[j]
                result[0] += temp
                return

            ans.append(nums[i])
            solve(i+1,ans)
            ans.pop()
            solve(i+1,ans)

        solve(0,[])
        return result[0]
