class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if k >= sum(diff):
            return 0

        low = 0
        high = max(diff)

        while low < high:
            mid = (low + high) // 2
            needed = sum(max(x - mid, 0) for x in diff)

            if needed <= k:
                high = mid
            else:
                low = mid + 1

        level = low
        needed = sum(max(x - level, 0) for x in diff)
        remaining = k - needed

        ans = 0

        for x in diff:
            ans += min(x, level) ** 2

        ans -= remaining * (2 * level - 1)

        return ans