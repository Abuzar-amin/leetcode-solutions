class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        k = k1 + k2
        total = 0
        max_diff = 0

        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            total += diff
            max_diff = max(max_diff, diff)

        if k >= total:
            return 0

        freq = [0] * (max_diff + 1)

        for a, b in zip(nums1, nums2):
            freq[abs(a - b)] += 1

        for diff in range(max_diff, 0, -1):
            if k == 0:
                break

            moves = min(freq[diff], k)
            freq[diff] -= moves
            freq[diff - 1] += moves
            k -= moves

        return sum(diff * diff * count
                   for diff, count in enumerate(freq))