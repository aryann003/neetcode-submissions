class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def solve(n, k, i, ans):
            if len(ans) == k:
                result.append(list(ans))
                return

            if i > n or len(ans) > k:
                return

            ans.append(i)
            solve(n, k, i + 1, ans)
            ans.pop()

            solve(n, k, i + 1, ans)

        solve(n, k, 1, [])
        return result