class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        start = 0
        end = mountainArr.length()-1

        while start < end:
            mid = (start + end)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                start = mid + 1
            else:
                end = mid 
        peak = start 


        l = 0
        r = peak

        while l <= r:
            mid = (l+r)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l = peak + 1
        r = mountainArr.length()-1

        while l <= r:
            mid = (l+r)//2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                r = mid - 1 
            else:
                l = mid + 1 
        return -1               