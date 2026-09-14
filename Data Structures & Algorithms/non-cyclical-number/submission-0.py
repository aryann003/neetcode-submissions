class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            res = 0
            while n > 0:
                rem = n % 10
                res += rem ** 2
                n = n // 10
            return res

        mp  = set()

        while n != 1:
            if n in mp:
                return False
            mp.add(n)

            n = square(n)
        
        return True