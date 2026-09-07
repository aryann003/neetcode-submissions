class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        st = set()
        start = 0
        mp = Counter(s)
        result = []

        for i in range(len(s)):
            mp[s[i]] -= 1
            if mp[s[i]] >= 1:
                st.add(s[i])
            if mp[s[i]] == 0 and s[i] in st:
                st.remove(s[i])
            if not st:
                result.append(i-start+1)
                start = i+1
        return result