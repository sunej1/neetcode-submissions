class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        parenthesis = self.generateParenthesis(n-1)
        sol = set()
        for p in parenthesis:
            for i in range(len(p) + 1):
                sol.add(p[:i] + "()" + p[i:])

        return list(sol)
