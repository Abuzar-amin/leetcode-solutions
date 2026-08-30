class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        front = 1
        back = 1
        minimum = nums[0]
        maximum = nums[0]
        for i in range(len(nums)):
            if minimum > nums[i]:
                minimum = nums[i]
            if maximum < nums[i]:
                maximum = nums[i]
        min_index = nums.index(minimum)
        max_index = nums.index(maximum)
        if min_index > max_index:
            min_index, max_index = max_index, min_index
        n = len(nums)
        front_only = max_index + 1
        back_only = n - min_index
        front_back_1 = (min_index + 1) + (n - max_index)
        front_back_2 = (max_index + 1) + (n - min_index)
        return min(front_only, back_only, front_back_1, front_back_2)
        
        


        