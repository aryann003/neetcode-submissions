class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def solve(n, ans, open, close):
            if len(ans) == 2*n:
                result.append("".join(ans))
                return 

            if open < n:
                ans.append('(')
                solve(n ,ans, open+1,close)
                ans.pop()

            if close < open:
                ans.append(')')
                solve(n,ans,open,close+1)
                ans.pop()
        ans = []
        solve(n, ans, 0 , 0)
        return result

            