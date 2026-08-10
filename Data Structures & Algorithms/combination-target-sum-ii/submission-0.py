class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        def solve(candidates, target, index, ans):
            if target == 0:
                result.append(list(ans))
                return

            if index == len(candidates) or target < 0:
                return

            ans.append(candidates[index])
            solve(candidates, target - candidates[index], index + 1, ans)
            ans.pop()

            # Store current value to skip all its occurrences
            current_val = candidates[index]
            index += 1

            while index < len(candidates) and candidates[index] == current_val:
                index += 1

            solve(candidates, target, index, ans)

        solve(candidates, target, 0, [])
        return result