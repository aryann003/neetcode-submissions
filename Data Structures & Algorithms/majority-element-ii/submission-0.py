class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = None
        cand2 = None
        cnt1 = 0
        cnt2 = 0

        for n in nums:
            if n == cand1:
                cnt1 += 1
            elif n == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = n
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        result = []
        size = len(nums)

        if nums.count(cand1) > size // 3:
            result.append(cand1)

        if cand2 != cand1 and nums.count(cand2) > size // 3:
            result.append(cand2)

        return result