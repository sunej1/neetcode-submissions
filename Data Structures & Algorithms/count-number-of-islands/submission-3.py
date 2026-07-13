class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        explored = set()

        count = 0

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if tuple([i, j]) not in explored:
                    if grid[i][j] == "1":
                        stack = [tuple([i,j])]
                        while stack:
                            popped = stack.pop()
                            for d in directions:
                                dir = [popped[0]+d[0], popped[1]+d[1]]
                                if 0 <= dir[0] < len(grid) and 0 <= dir[1] < len(grid[0]) and grid[dir[0]][dir[1]] == "1" and tuple(dir) not in explored:
                                    stack.append(tuple(dir))
                                    explored.add(tuple(dir))
                        count += 1
                explored.add(tuple([i,j]))
        return count
                

