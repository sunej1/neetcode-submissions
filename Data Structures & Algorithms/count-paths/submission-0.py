class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        memo[tuple([m-1, n-1])] = 1

        def helperMethod(i: int, j: int) -> int:
            if tuple([i, j]) in memo:
                return memo[tuple([i, j])]
            else:
                if i+1 < m and j+1 < n:
                    memo[tuple([i, j])] = helperMethod(i+1, j) + helperMethod(i, j+1)
                elif i+1 < m and j+1 >= n:
                    memo[tuple([i, j])] = helperMethod(i+1, j)
                elif i+1 >= m and j+1 < n:
                    memo[tuple([i, j])] = helperMethod(i, j+1)
                else:
                    memo[tuple([i, j])] = 1
                return memo[tuple([i, j])]
        
        memo[tuple([0, 0])] = helperMethod(0, 0)
        return memo[tuple([0, 0])]