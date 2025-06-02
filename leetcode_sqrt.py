# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return high


sol = Solution()
print(sol.mySqrt(4))
