class UnionFind:

    def __init__(self, n: int):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.num_components = n

    def find(self, x: int) -> int:
        p = x
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
        # Could replace p with x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.rank[p2] += self.rank[p2]
            self.rank[p1] = self.rank[p1]
            self.parent[p1] = self.parent[p2]
        else:
            self.rank[p1] += self.rank[p1]
            self.rank[p2] = self.rank[p2]
            self.parent[p2] = self.parent[p1]
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
