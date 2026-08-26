class Solution: 
    def reverse(self, x: int) -> int: 
        r = 0 
        sign = 0 
        if x < 0: 
            x = (-x) 
            sign = 1 
        while x: 
            r = (r * 10) +  x%10 
            x = x // 10 
        if sign: 
            r  = -r 
        if r > (2 ** 31) - 1 or r < -2 ** 31: 
            r = 0 
 
        return r
 
        