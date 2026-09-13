from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        a = [(i, j)
             for i in range(n)
             for j in range(n)
             if img1[i][j]]

        b = [(i, j)
             for i in range(n)
             for j in range(n)
             if img2[i][j]]

        shifts = Counter()

        for x1, y1 in a:
            for x2, y2 in b:
                shifts[(x2 - x1, y2 - y1)] += 1

        return max(shifts.values(), default=0)