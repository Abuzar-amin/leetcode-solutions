class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            seen = set()
            distinct = 0

            for j in range(i, n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    distinct += 1

                ans += distinct * distinct

        return ans
