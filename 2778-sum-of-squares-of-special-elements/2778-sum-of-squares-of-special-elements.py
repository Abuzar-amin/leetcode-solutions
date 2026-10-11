class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for i in range(len(nums)):
            if n % (i+1) == 0:
                sum += nums[i]*nums[i]
        print(sum)
        return sum
        