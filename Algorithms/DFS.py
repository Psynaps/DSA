# Implementation of dfs in a grid to could the number of paths
# from the source (top left) to destination (bottom right)


class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == 1
                or (r, c) in visit
            ):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            visit.add((r, c))

            count = 0
            count += dfs(r + 1, c, visit)
            count += dfs(r - 1, c, visit)
            count += dfs(r, c + 1, visit)
            count += dfs(r, c - 1, visit)
            visit.remove((r, c))
            return count

        return dfs(0, 0, set())
