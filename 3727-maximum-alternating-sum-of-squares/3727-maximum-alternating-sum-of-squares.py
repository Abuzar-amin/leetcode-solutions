
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        count = [0] * 40001
        total = 0

        for num in nums:
            num = abs(num)
            count[num] += 1
            total += num * num

        subtract = 0
        remaining = len(nums) // 2

        for num in range(40001):
            take = min(count[num], remaining)
            subtract += take * num * num
            remaining -= take

            if remaining == 0:
                break

        return total - 2 * subtract
