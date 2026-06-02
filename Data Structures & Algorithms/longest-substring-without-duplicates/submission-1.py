class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        start = 0
        max_length  = 0
        for i in range(len(s)):
            while s[i] in st:
                    st.remove(s[start])
                    start += 1
            
            st.add(s[i])
            length = i-start+1

            max_length = max(max_length,length)

        return max_length
