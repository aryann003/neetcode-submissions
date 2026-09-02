class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ %2 != 0:
            return False
        
        target = summ // 2

        def solve(index, target):
            if index == len(nums) or target < 0:
                return False
            if target == 0:
                return True
            
            return solve(index+1,target-nums[index]) or solve(index+1,target)

        return solve(0,target)
