from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def solve(index, count):
            if count < 0:
                return False
            if index == len(s):
                if count == 0:
                    return True
                return False
            
            if s[index] == "(":
                return solve(index+1,count+1)
            elif s[index] == ")":
                return solve(index+1,count-1)
            else:
                return solve(index+1,count+1) or solve(index+1,count-1) or solve(index+1,count)

            return False

        return solve(0,0)