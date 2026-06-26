class Solution:
    def helperMethod(self, n: int, memo: dict) -> int:
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.helperMethod(n-1, memo) + self.helperMethod(n-2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        return self.helperMethod(n, memo)

        