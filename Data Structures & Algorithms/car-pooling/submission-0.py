class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        arr = [0]*1000

        for p, f, t, in trips:
            arr[f] += p
            arr[t] -= p
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            if curr > capacity:
                return False
        return True