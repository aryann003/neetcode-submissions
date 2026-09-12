class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""

        length_1 = len(str1)

        while length_1 > 0:
            if len(str1) % length_1 == 0 and len(str2) % length_1 == 0:
                return str1[:length_1]
            
            length_1 -= 1
        return ""


    