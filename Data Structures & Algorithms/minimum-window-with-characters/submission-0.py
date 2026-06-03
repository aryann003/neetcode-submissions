class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        m1 = {}
        m2 = {}

        for c in t:
            m1[c] = m1.get(c,0)+1

        start = 0
        start_idx= 0
        min_length = float('inf')
        have = 0
        need = len(m1)
        for end in range(len(s)):
            ch = s[end]

            m2[ch] = m2.get(ch,0)+1

            if ch in m1 and m1[ch] == m2[ch]:
                have += 1

            while have == need:
                length = end - start + 1
                if length < min_length:
                    min_length = length
                    start_idx = start
                m2[s[start]] -= 1

                if s[start] in m1 and m2[s[start]] < m1[s[start]]:
                    have -= 1
                start += 1
        if min_length == float('inf'):
            return ""
        return s[start_idx:min_length+start_idx]
        