class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        prev = 0
        curr = 1 

        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                direction = 1
            elif arr[i] < arr[i-1]:
                direction = -1
            else:
                direction = 0
            if direction == 0:
                curr = 1
            elif direction != prev:
                curr += 1
            else:
                curr = 2
            prev = direction
            ans = max(ans,curr)

        return ans