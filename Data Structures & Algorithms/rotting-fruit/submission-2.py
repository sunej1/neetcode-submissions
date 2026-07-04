from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.append([row, col])
        queue.append([-1, -1])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1 and col == -1:
                if not queue:
                    continue
                else:
                    count += 1
                    queue.append([-1, -1])
            for dr, dc in directions:
                curr = [dr+row, dc+col]
                if 0 <= curr[0] < len(grid) and 0 <= curr[1] < len(grid[0]) and grid[curr[0]][curr[1]] == 1:
                        grid[curr[0]][curr[1]] = 2
                        queue.append([curr[0], curr[1]])

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1
        return count