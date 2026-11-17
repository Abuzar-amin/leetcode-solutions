class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute proper divisors
        divisors = [[] for _ in range(n + 1)]

        for d in range(1, n):
            for length in range(d * 2, n + 1, d):
                divisors[length].append(d)

        # Precompute cost for every substring
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = n

                for d in divisors[length]:
                    changes = 0

                    for offset in range(d):
                        left = i + offset
                        right = j - d + 1 + offset

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # Suffix DP
        dp = [[n] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for parts in range(1, k + 1):
                for j in range(i + 1, n):
                    dp[i][parts] = min(
                        dp[i][parts],
                        cost[i][j] + dp[j + 1][parts - 1]
                    )

        return dp[0][k]
