class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minimum = float('inf')

        for i in range(len(nums)):
            total = 0

            for j in range(i, min(i + r, len(nums))):
                total += nums[j]

                if j - i + 1 >= l and total > 0:
                    minimum = min(minimum, total)

        return minimum if minimum != float('inf') else -1