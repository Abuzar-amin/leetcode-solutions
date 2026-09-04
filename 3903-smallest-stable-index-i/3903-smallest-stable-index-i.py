class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        i = 0
        maximum = 0
        minimum = 0
        instability_score = []
        while i < len(nums):
            maximum = max(nums[0:i+1])
            minimum = min(nums[i:len(nums)])
            instability_score.append(maximum - minimum)
            i+=1
        print(instability_score)
        for j in range(len(instability_score)):
            if instability_score[j] <= k:
                return instability_score.index(instability_score[j])
        return -1 

        