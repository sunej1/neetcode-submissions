class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0

        def helperMethod(a: int) -> int:
            if a in memo:
                return memo[a]
            elif a < 0:
                return -1
            else:
                temp = []
                for i in range(len(coins)):
                    t = helperMethod(a-coins[i])
                    if t!= -1:
                        temp.append(t+1)
                if len(temp) == 0:
                    memo[a] = -1
                    return -1
                memo[a] = min(temp)
                return memo[a]
                
        return helperMethod(amount)
