class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=0
        count = 0
        for i in range(len(nums)):
            if val != nums[i]:
                count+=1
                nums[j] = nums[i]
                j+=1
        
        return count