class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node: int, par: int) -> bool:
            if node in visited:
                return False

            visited.add(node)
            for nod in adj[node]:
                if nod == par:
                    continue
                if not dfs(nod, node):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n
                