class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flag = [False] * 3
        for trip in triplets:
            if all(trip[i] <= target[i] for i in range(3)):
                for i in range(3):
                    if trip[i] == target[i]:
                        flag[i] = True

        return all(flag)
           