class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                for b in dp[i][j]:
                    for x, y in ((i + 1, j), (i, j + 1)):
                        if x < m and y < n:
                            nb = b + (1 if grid[x][y] == '(' else -1)
                            if nb >= 0:
                                dp[x][y].add(nb)

        return 0 in dp[-1][-1]