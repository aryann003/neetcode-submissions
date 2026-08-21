class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        words = set(wordDict)

        def solve(i,ans):
            if i == len(s):
                result.append(" ".join(ans))
                return
            
            for j in range(i,len(s)):
                word = s[i:j+1]

                if word in words:
                    ans.append(word)
                    solve(j+1,ans)
                    ans.pop()
        solve(0,[])
        return result
