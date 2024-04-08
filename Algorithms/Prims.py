import heapq


class Solution:
    def minimumSpanningTree(self, n: int, edges: list[list[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for src, dst, w in edges:
            adj[src].append([dst, w])  # it is an undirected graph
            adj[dst].append([src, w])

        MST_weight = 0
        MST = []  # Not needed since we only need the MST weight
        # If the actual MST is desired, then have edges in heap contain both src and destination
        # So that the edge can be added to the MST, not just the weight of the edge

        start = 0

        # frontier_edges = [[0, 0]]
        frontier_edges = []
        for neighbor, w in adj[start]:
            heapq.heappush(frontier_edges, (w, start, neighbor))

        visited = set()  # could also be an array of size n
        visited.add(0)

        while frontier_edges and len(visited) < n:
            weight, src, dst = heapq.heappop(frontier_edges)

            if dst in visited:  # Don't have to check whether src is in MST,
                # since if it was added to the heap then src is in the MST
                continue

            MST_weight += weight
            MST.append((src, dst))
            visited.add(dst)

            # add new possible edges to the frontier_edges heap
            for neighbor, w in adj[dst]:
                if neighbor not in visited:
                    heapq.heappush(frontier_edges, (w, dst, neighbor))

        # Have edges of MST in MST var
        print("MST:", MST)

        return MST_weight if len(visited) == n else -1


# Test cases
solution = Solution()
# Example 1
n = 5
edges = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]
res = solution.minimumSpanningTree(n, edges)
print(res == 11)
