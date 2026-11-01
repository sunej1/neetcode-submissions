class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        memo[len(cost)-1] = cost[len(cost)-1]
        memo[len(cost)-2] = cost[len(cost)-2]

        def helperMethod(i: int) -> int:
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(helperMethod(i+1), helperMethod(i+2))
            return memo[i]
            
        memo[0] = helperMethod(0)
        memo[1] = helperMethod(1)
        return min(memo[0], memo[1])