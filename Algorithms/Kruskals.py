# Implementation of Kruskals algorithm with Union Find to find the minimum spanning tree of an undirected graph

import heapq


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        # if x != self.parent[x]:
        #     self.parent[x] = self.find(self.parent[x])
        # return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False

        if self.size[p1] < self.size[p2]:
            self.size[p2] += self.size[p1]
            self.parent[p1] = p2
        else:
            self.size[p1] += self.size[p2]
            self.parent[p2] = p1
        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: list[list[int]]) -> int:
        min_heap = []
        for n1, n2, w in edges:
            heapq.heappush(min_heap, (w, n1, n2))

        unionFind = UnionFind(n)
        res, components = 0, n

        while components > 1 and min_heap:
            w, n1, n2 = heapq.heappop(min_heap)
            if unionFind.union(n1, n2):
                res += w
                components -= 1

        return res if components == 1 else -1
