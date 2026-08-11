class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1

            return True

        def solve(s, index, ans):
            if index == len(s):
                result.append(list(ans))
                return

            for end in range(index, len(s)):
                if palindrome(s, index, end):
                    ans.append(s[index:end + 1])

                    solve(s, end + 1, ans)

                    ans.pop()

        solve(s, 0, [])

        return result