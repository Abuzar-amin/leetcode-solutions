class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i = 0
        j = 0
        median = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                nums3.append(nums2[j])
                j += 1
            else:
                nums3.append(nums1[i])
                nums3.append(nums2[j])
                i +=1
                j +=1
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1
        print(nums3)
        if len(nums3) % 2 == 0:
            length = len(nums3)//2
            median = (nums3[length-1] + nums3[length]) / 2
        else:
            length = len(nums3)//2
            median = nums3[length]
        return median

        