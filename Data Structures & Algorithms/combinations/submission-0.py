class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []


        def solve(n,i, ans):
            if len(ans) == k:
                result.append(list(ans))
                return
            if i > n:
                return 

            ans.append(i)
            solve(n,i+1,ans)
            ans.pop()
            solve(n,i+1,ans)
        ans = []
        solve(n,1,ans)
        return result