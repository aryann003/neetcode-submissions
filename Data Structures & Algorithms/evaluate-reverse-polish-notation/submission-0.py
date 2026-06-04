class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for ch in tokens:
            if ch.isdigit() or (len(ch) > 1 and ch[0] == '-'):
                st.append(int(ch))
            else:
                op = ch
                num1 = st[-1]
                st.pop()
                num2 = st[-1]
                st.pop()

                if op == '+':
                    st.append(num2 + num1)
                elif op == '-':
                    st.append(num2-num1)
                elif op == '*':
                    st.append(num2*num1)
                else:
                    st.append(int(num2/num1))

        return st[-1]