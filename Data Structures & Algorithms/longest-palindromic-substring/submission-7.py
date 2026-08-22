class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        max_length = 0
        ans = ""
        for end in range(len(s)):


            i,j = end,end

            while i>=0 and j<len(s):
                if s[i] == s[j]:
                    length = j-i+1
                    if length > max_length:
                        max_length = length
                        ans = s[i:j+1]
                    i -= 1
                    j += 1
                else:
                    break

            i,j = end,end+1

            while i>=0 and j<len(s):
                if s[i] == s[j]:
                    length = j-i+1
                    if length>max_length:
                        max_length = length
                        ans = s[i:j+1]
                    i -= 1
                    j += 1

                else:
                    break

        return ans
