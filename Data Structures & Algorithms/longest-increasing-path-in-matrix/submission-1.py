class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        lens = set()

        def helperMethod(row: int, col: int) -> int:
            s = set()
            if memo[row][col] != -1:
                return memo[row][col]
            else:
                for dir in directions:
                    if 0 <= dir[0]+row < len(matrix) and 0 <= dir[1]+col < len(matrix[0]) and matrix[dir[0]+row][dir[1]+col] > matrix[row][col]:
                        s.add(helperMethod(dir[0]+row, dir[1]+col))

                if len(s) == 0:
                    memo[row][col] = 1
                else:
                    memo[row][col] = 1+max(s)
                return memo[row][col]


        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                lens.add(helperMethod(row, col))

        return max(lens)