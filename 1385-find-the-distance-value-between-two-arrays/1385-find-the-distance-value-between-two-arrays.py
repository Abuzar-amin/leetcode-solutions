class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for num in arr1:
            valid = True

            for other in arr2:
                if abs(num - other) <= d:
                    valid = False
                    break

            if valid:
                ans += 1

        return ans
