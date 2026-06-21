class Solution:
    def checkValidString(self, s: str) -> bool:
        p = []
        st = []
        for i in range(len(s)):
            if s[i] == "*":
                st.append(i)
            elif s[i] == "(":
                p.append(i)
            else:
                if len(p) > 0:
                    p.pop()
                elif len(st) > 0:
                    st.pop()
                else:
                    return False
        while p and st:
            if p[-1] > st[-1]:
                return False
            p.pop()
            st.pop()

        return len(p) == 0
