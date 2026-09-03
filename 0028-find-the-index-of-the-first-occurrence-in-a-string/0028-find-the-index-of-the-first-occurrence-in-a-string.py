class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        if needle not in haystack:
            index = -1
        else:
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i + len(needle)] == needle:
                    index = i
                    break

                
        return index