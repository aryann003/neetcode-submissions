from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        @cache
        def solve(index):
            if index == len(s):
                return True

            for i in range(index+1,len(s)+1):
                word = s[index:i]
                if word in words and solve(i):
                    return True
            
            return False
        return solve(0)        
                