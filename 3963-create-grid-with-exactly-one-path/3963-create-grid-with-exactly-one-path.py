class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]

        for i in range(m):
            grid[i][0] = '.'

        grid[m - 1] = ['.'] * n

        return [''.join(row) for row in grid]