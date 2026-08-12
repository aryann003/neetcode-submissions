class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
    
        total = sum(matchsticks)

        if total % 4 != 0:
            return False
        
        target = total//4

        if max(matchsticks) > target:
            return False

        sides = [0]*4

        def solve(index):
            if index == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[index] <= target:
                    sides[j] += matchsticks[index]
                    if solve(index+1):
                        return True

                    sides[j] -= matchsticks[index]

            return False

        return solve(0)
