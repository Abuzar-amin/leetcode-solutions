class Solution:
    def reverse(self, x: int) -> int:
        a=[]
        sign = 0
        if x < 0:
            x = (-x)
            sign = 1
        while x // 10 != 0:
            a.append(x % 10)
            x = x // 10
        a.append(x)
        x = 0
        for i in range(len(a)):
            x += a[i] * (10 ** (len(a)-i-1))
        if sign:
            x  = -x
        if x > (2 ** 31) - 1 or x < -2 ** 31:
            x = 0

        return x

        