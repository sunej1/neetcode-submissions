from functools import cache
class Solution:
    @cache 
    def climbStairs(self, n: int) -> int:
        if n > 2:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        elif n == 2:
            return 2
        else:
            return 1