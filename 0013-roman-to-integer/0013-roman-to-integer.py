class Solution:
    def romanToInt(self, s: str) -> int:
        r = 0
        Roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }
        if "IV" in s:
            r += 4
            s = s.replace("IV", "")
        if "IX" in s:
            r += 9
            s = s.replace("IX", "")
        if "XL" in  s:
            r += 40
            s = s.replace("XL", "")
        if "XC" in s:
            r += 90
            s = s.replace("XC", "")
        if "CD" in s:
            r += 400
            s = s.replace("CD", "")
        if "CM" in s:
            r += 900
            s = s.replace("CM", "") 
        for i in range(len(s)):
            r += Roman[s[i]]
        return r

        