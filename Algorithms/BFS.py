# Implementation of bfs in a grid to find the length of the shortest path from
# the source (top left) to destination (bottom right)

from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        count = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return count
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if (
                        (r + dr) not in range(ROWS)
                        or (c + dc) not in range(COLS)
                        or grid[r + dr][c + dc] == 1
                        or (r + dr, c + dc) in visited
                    ):
                        continue
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            count += 1
        return -1
