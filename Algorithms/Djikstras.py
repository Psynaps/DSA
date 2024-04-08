# Djikstra's Algorithm on a directed graph with non-negative weights

import heapq


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        # Step 1: Create the adjacency list
        adj_list = {i: [] for i in range(n)}
        for s, d, w in edges:
            adj_list[s].append((d, w))

        # Step 2: Initialize distances
        distance = {i: float("inf") for i in range(n)}
        distance[src] = 0

        # Step 3: Initialize the priority queue
        pq = [(0, src)]

        # Step 4: Process nodes in the priority queue
        while pq:
            dist, node = heapq.heappop(pq)
            if dist != distance[node]:
                continue
            for neighbor, weight in adj_list[node]:
                new_dist = dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        # Step 5: Replace distances to unreachable nodes with -1
        for node in distance:
            if distance[node] == float("inf"):
                distance[node] = -1

        # Step 6: Return the distance dictionary
        return distance

    def shortestPath2(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for s, dst, w in edges:
            adj_list[s].append([dst, w])

        shortest = {}
        min_heap = [[0, src]]

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj_list[n1]:  # for each neighbor of n1
                if n2 not in shortest:
                    heapq.heappush(min_heap, [w1 + w2, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


# Test Cases
solution = Solution()
# Example 1
n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
# Expected: {0: 0, 1: 100, 2: 200}
print("soln1", solution.shortestPath(n, edges, src))
print("soln2", solution.shortestPath2(n, edges, src))
# Example 2
n = 4
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500], [1, 3, 50], [2, 3, 10]]
src = 0
print("----------------")
print("soln1", solution.shortestPath(n, edges, src))
print("soln2", solution.shortestPath2(n, edges, src))
# Expected: {0: 0, 1: 100, 2: 200, 3: -1}


n = 4
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500], [3, 1, 50]]
src = 0
# print(solution.shortestPath(4, edges, src))
print("----------------")
print("soln1", solution.shortestPath(n, edges, src))
print("soln2", solution.shortestPath2(n, edges, src))
