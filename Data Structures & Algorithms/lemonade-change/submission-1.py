class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0

        for b in bills:
            if b == 5:
                count5 += 1
            if b == 10:
                if count5 > 0 :
                    count5 -= 1
                    count10 += 1
                else:
                    return False
            if b == 20:
                if count5 > 0 and count10:
                    count5 -= 1
                    count10 -=1
                elif count5 > 2:
                    count5 -= 3
                else:
                    return False

        return True  
