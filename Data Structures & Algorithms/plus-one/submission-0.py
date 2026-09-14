class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0

        for i in digits:
            num = num *10 + i

        num = num + 1
        res = []
        while num > 0:
            rem = num %10
            res.append(rem)
            num = num // 10
        res.reverse()
        return res
    

            