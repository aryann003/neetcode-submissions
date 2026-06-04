class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids:
            if ast > 0:
                st.append(ast)

            else:
                while st and st[-1] > 0 and st[-1] < abs(ast):
                    st.pop()

                if not st or st[-1] < 0:
                    st.append(ast)
                elif st[-1] == abs(ast):
                    st.pop()
        return st