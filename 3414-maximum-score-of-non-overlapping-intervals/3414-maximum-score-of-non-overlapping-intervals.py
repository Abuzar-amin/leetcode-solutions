from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Keep original indices
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        # Previous non-overlapping interval
        prev = [
            bisect_left(ends, arr[i][0]) - 1
            for i in range(n)
        ]

        # dp[k][i] = best (weight, indices) using first i intervals
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]

            for k in range(1, 5):
                # Don't take current interval
                best = dp[k][i - 1]

                # Take current interval
                p = prev[i - 1] + 1
                old_weight, old_indices = dp[k - 1][p]

                candidate = (
                    old_weight + w,
                    old_indices + (idx,)
                )

                if candidate[0] > best[0]:
                    best = candidate
                elif candidate[0] == best[0]:
                    if sorted(candidate[1]) < sorted(best[1]):
                        best = candidate

                dp[k][i] = best

        return sorted(dp[4][n][1])