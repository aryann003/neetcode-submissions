class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        result = []
        if len(digits) == 0:
            return []

        def combinations(mp,index,ans):
            if index == len(digits):
                result.append("".join(ans))
                return

            value = int(digits[index])
            letter = mp[value]

            for i in range(len(letter)):
                ans.append(letter[i])
                combinations(mp,index+1,ans)
                ans.pop()

        ans = []

        combinations(mp,0,ans)
        return result



