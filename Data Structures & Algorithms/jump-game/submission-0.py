class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i,j = len(nums)-1,len(nums)-1
    
        while j >= 0:
            if j+nums[j] >= i:
                i = j
            j-=1
            
        
        return i == 0
            
