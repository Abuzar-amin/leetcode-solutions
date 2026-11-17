class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # cost[i][j] = minimum changes to make s[i:j+1]
        # a semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = float('inf')

                # Try every proper divisor of length
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Compare mirrored positions in each group
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

        # dp[i][parts] = minimum changes to divide
        # the first i characters into parts substrings
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                for start in range(i - 1):
                    if dp[start][parts - 1] == float('inf'):
                        continue

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[start][parts - 1] + cost[start][i - 1]
                    )

        return dp[n][k]
