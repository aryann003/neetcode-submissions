class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0

        for end in range(len(s)):

            # Odd length palindromes
            i, j = end, end

            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    count += 1
                    i -= 1
                    j += 1
                else:
                    break

            # Even length palindromes
            i, j = end, end + 1

            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    count += 1
                    i -= 1
                    j += 1
                else:
                    break

        return count