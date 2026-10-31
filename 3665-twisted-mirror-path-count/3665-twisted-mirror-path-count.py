
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp_right = [[0] * n for _ in range(m)]
        dp_down = [[0] * n for _ in range(m)]

        dp_right[0][0] = 1

        for i in range(m):
            for j in range(n):
                r = dp_right[i][j]
                d = dp_down[i][j]

                if grid[i][j] == 0:
                    if j + 1 < n:
                        dp_right[i][j + 1] += r + d
                        dp_right[i][j + 1] %= mod

                    if i + 1 < m:
                        dp_down[i + 1][j] += r + d
                        dp_down[i + 1][j] %= mod

                else:
                    if i + 1 < m:
                        dp_down[i + 1][j] += r
                        dp_down[i + 1][j] %= mod

                    if j + 1 < n:
                        dp_right[i][j + 1] += d
                        dp_right[i][j + 1] %= mod

        return (dp_right[m - 1][n - 1] + dp_down[m - 1][n - 1]) % mod
