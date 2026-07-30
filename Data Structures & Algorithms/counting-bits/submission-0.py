class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        lst.append(0)
        for i in range(1,n+1):
            cnt = 0
            while i:
                i = i &(i-1)
                cnt += 1
            lst.append(cnt)
        return lst

