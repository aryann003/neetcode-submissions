class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        m1 = {}
        m2 = {}
        for c in s1:
            if c in m1:
                m1[c] += 1
            else:
                m1[c] = 1
        window = len(s1)
        for i in range(len(s2)):
            m2[s2[i]] = m2.get(s2[i],0)+1

            if i >= window:
                left_char = s2[i-window]
                m2[left_char] -= 1

                if m2[left_char] == 0:
                    del m2[left_char]

            if m1 == m2:
                return True
        return False

        