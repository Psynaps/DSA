# Implementation of a Topological Sort algorithm using Depth First Search


class Solution:
    def topologicalSort(self, n: int, edges: list[list[int]]) -> list[int]:
        adj = {i: [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)

        visited = set()
        visiting = set()
        topo_sort = []

        def dfs(node: int) -> bool:
            if node in visited:
                return True
            if node in visiting:
                return False

            visiting.add(node)

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            visiting.remove(node)
            visited.add(node)
            topo_sort.append(node)

            return True  # No cycle

        for i in range(n):
            if not dfs(i):
                return []  # cycle detected

        topo_sort.reverse()
        return topo_sort
