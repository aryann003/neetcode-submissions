class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            else:
                if not st:
                    return False
                elif st[-1] == '(' and c == ')':
                    st.pop()
                elif st[-1] == '{' and c == '}':
                    st.pop()
                elif st[-1] == '[' and c == ']':
                    st.pop()
                else:
                    return False

        return len(st) == 0