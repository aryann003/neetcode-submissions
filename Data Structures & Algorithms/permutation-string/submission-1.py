class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        m1 = {}
        for c in s1:
            if c in m1:
                m1[c] += 1
            else:
                m1[c] = 1

        start = 0
        end = len(s1)-1

        while end < len(s2):
            m2 = {}

            for i in range(start,end+1):
                if s2[i] in m2:
                    m2[s2[i]] += 1
                else:
                    m2[s2[i]] = 1

            if m1 == m2:
                return True
            end += 1
            start += 1

        return False

        