class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        distance = {i: float("inf") for i in range(n)}
        distance[src] = 0

        for _ in range(n - 1):
            for src, dst, w in edges:
                if distance[src] != float("inf") and distance[src] + w < distance[dst]:
                    distance[dst] = distance[src] + w

        # set infinity to -1
        for key in distance:
            if distance[key] == float("inf"):
                distance[key] = -1

        return distance


# Test Cases
solution = Solution()
# Example 1
n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
# Expected: {0: 0, 1: 100, 2: 200}
print(solution.shortestPath(n, edges, src))
# Example 2
n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500], [2, 1, 50], [1, 0, 50]]
src = 2
print(solution.shortestPath(n, edges, src))
# Expected: {0: 100, 1: 50, 2: 0}
