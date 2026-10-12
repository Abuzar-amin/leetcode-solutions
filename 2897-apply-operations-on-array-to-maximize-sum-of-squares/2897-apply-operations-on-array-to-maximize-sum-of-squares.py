class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 30

        for num in nums:
            for bit in range(30):
                if num & (1 << bit):
                    cnt[bit] += 1

        ans = 0

        for _ in range(k):
            num = 0

            for bit in range(30):
                if cnt[bit] > 0:
                    num |= 1 << bit
                    cnt[bit] -= 1

            ans = (ans + num * num) % mod

        return ans