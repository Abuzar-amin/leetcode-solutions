class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            x = num % k

            # Start a new subarray
            new_dp[x] += 1

            # Extend previous subarrays
            for r in range(k):
                new_r = (r * x) % k
                new_dp[new_r] += dp[r]

            # Add to final answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans