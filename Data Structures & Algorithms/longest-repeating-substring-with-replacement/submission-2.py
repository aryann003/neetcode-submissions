class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        char = set(s)
        for c in char:
            j = 0
            cnt = 0
            for i in range(len(s)):
                if s[i] != c:
                    cnt += 1

                while cnt > k:
                    if s[j] != c:
                        cnt -= 1
                    j += 1
                max_length = max(max_length,i-j+1)
        return max_length



