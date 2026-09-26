class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle sign
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            chunk = divisor
            count = 1

            # Keep doubling until the next doubling is too large
            while dividend >= chunk + chunk:
                chunk += chunk
                count += count

            dividend -= chunk
            result += count

        if negative:
            result = -result

        # 32-bit integer limit
        return max(-2**31, min(2**31 - 1, result))