class Solution:
    def reverse(self, x: int) -> int:
        minus = 1
        if x < 0:
            minus = -1
            x = -x
        y = x % 10
        while x // 10 > 0:
            x = x // 10
            y = (y * 10) + (x % 10)
        y = minus * y
        if y <= -2**31 or y >= 2**31-1:
            return 0
        return y
a = Solution()
print(a.reverse(1534236469))
print(a.reverse(-2147483412))

