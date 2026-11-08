class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rows = [sum(row) for row in grid]
        cols = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    if rows[i] > 1:
                        ans += 1
                    elif cols[j] > 1:
                        ans += 1

        return ans
