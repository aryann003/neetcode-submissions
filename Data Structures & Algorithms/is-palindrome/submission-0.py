class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
        
        first = 0
        last = len(res) - 1
        while first < last:
            if res[first] != res[last]:
                return False
            first += 1
            last -= 1
        return True