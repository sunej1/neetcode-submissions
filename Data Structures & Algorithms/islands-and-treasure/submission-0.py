from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    treasures.append([row, col])
        for t in treasures:
            t=tuple(t)
            visited = set()
            queue = deque(t)
            visited.add(t)


            while queue:
                row = queue.popleft()
                col = queue.popleft()
                
                if row+1 < len(grid) and tuple([row+1, col]) not in visited:
                    visited.add(tuple([row+1, col]))
                    if grid[row+1][col] != -1:
                        queue.append(row+1)
                        queue.append(col)
                        if grid[row+1][col] > grid[row][col]+1:
                            grid[row+1][col] = grid[row][col]+1
                if row-1 >= 0 and tuple([row-1, col]) not in visited:
                    visited.add(tuple([row-1, col]))
                    if grid[row-1][col] != -1:
                        queue.append(row-1)
                        queue.append(col)
                        if grid[row-1][col] > grid[row][col]+1:
                            grid[row-1][col] = grid[row][col]+1
                if col+1 < len(grid[0]) and tuple([row, col+1]) not in visited:
                    visited.add(tuple([row, col+1]))
                    if grid[row][col+1] != -1:
                        queue.append(row)
                        queue.append(col+1)
                        if grid[row][col+1] > grid[row][col]+1:
                            grid[row][col+1] = grid[row][col]+1
                if col-1 >= 0 and tuple([row, col-1]) not in visited:
                    visited.add(tuple([row, col-1]))
                    if grid[row][col-1] != -1:
                        queue.append(row)
                        queue.append(col-1)
                        if grid[row][col-1] > grid[row][col]+1:
                            grid[row][col-1] = grid[row][col]+1

        